# Please use Python version 2.7

# This script web-scrapes recipe information from cookpad

# author: Richard Kunert (rikunert@gmail.com) July 2017

from BeautifulSoup import BeautifulSoup  # for website parsing
import requests  # for http access
import pickle #for saving

#custom functions
def recipe_page_parse(address, header_info):

    print '<><><><><><><><>' + address

    #retrieve and then parse the html tree
    soup = BeautifulSoup(requests.get(address).text)

    #not all recipes include portions information
    if soup('div', {'data-field-name':'serving'}):
        portions = soup('div', {'data-field-name':'serving'})[0].text
    else:
        portions = 'NaN'

    #not all recipes include cooking time information
    if soup('div', {'data-field-name':'cooking_time'}):
        cooking_time = soup('div', {'data-field-name':'cooking_time'})[0].text
    else:
        cooking_time = 'NaN'

    #create a dictionary with all the information one could wish to have about this recipe
    x = {
        'super_grouping' : header_info['super_grouping'],
        'sub_grouping' : header_info['sub_grouping'],
        'address' : address,
        'title' : soup('h1')[0].text,
        'likes' : soup('div', {'class':'recipe-show__metadata'})[0].text,
        'user' : soup('span', {'itemprop':'author'})[0].text,
        'ingredients': [ingredient_with_quantity.replace(ingredient_quantity,'')
                        for ingredient_with_quantity, ingredient_quantity in
                        zip([link.text for link in soup('div', {'class':'ingredient__details'})],
                            [link.text for link in soup('span', {'class': 'ingredient__quantity'})])],
        'portions' : portions,
        'cooking_time': cooking_time}

    return x

#The highest level cookpad page which will hopefully get us access to all recipes
soup = BeautifulSoup(requests.get('https://cookpad.com/us/search_categories').text)#

#use attributes which characterise tags to identify tags correctly
recipe_section = soup('div', {'class' : 'col-md-3'})#all sections (<div>) whose class equals col-md-3

#go through all col-md-r sections and extract all the info we need
recipe_info = []
for i in range(len(recipe_section)): # for each super-grouping of recipes, e.g., Meal
    print '<><>Super-grouping: ' + recipe_section[i].find('h3').text

    links1 = [link.get('href') for link in recipe_section[i]('a')]

    for j in range(len(recipe_section[i]('a'))): #for each sub-grouping of recipes, e.g., Breakfast
        print '<><><><>Sub-grouping: ' + recipe_section[i]('div', {'class':'media__body'})[j].text

        #all recipes which follow have this info in common
        header_info = {'super_grouping' : recipe_section[i].find('h3').text,
                       'sub_grouping' : recipe_section[i]('div', {'class':'media__body'})[j].text}

        recipes_link = links1[j]

        counter = 0
        while True:#loop through all individual recipes
            counter = counter + 1
            print '<><><><><><>page ' + str(counter) + ' of ' + recipe_section[i]('div', {'class':'media__body'})[j].text

            soup = BeautifulSoup(
                requests.get('https://cookpad.com' + recipes_link).text)  # parse page within this sub-grouping

            links2 = [link.get('href') for link in soup('a', {'class' : 'media'})]  # all links to recipes excluding tags
            recipe_info = recipe_info + [recipe_page_parse('https://cookpad.com' + link, header_info) for link in links2]

            if len(soup('a', {'rel': 'next'})) != 0:
                recipes_link = soup('a', {'rel': 'next'})[0].get('href')#link to next page
            else:
                break#leave the while loop

        # save what we have so far (pickled)
        with open('cookpad_recipe_info_' + recipe_section[i]('div', {'class':'media__body'})[j].text + '.pickled', 'wb') as fp:
            pickle.dump(recipe_info, fp)
    recipe_info = []

        # to read it later:
        # with open ('cookpad_recipe_info.pickled', 'rb') as fp:
        #    recipe_info = pickle.load(fp)
