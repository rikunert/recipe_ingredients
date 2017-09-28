def ingredient_translator(recipe_info):
    """This function creates common words for synonymous ingredient names"""

    for c1, r in enumerate(recipe_info):  # for each recipe r and its counter c
        for c2, i in enumerate(r['ingredients']):  # for each ingredient of this recipe

            # SPICES

            if i.lower() in ['sea salt', 'seasoning salt', 'salt to taste', 'season salt', 'kosher salt',
                             'seasoned salt', 'tea spoon salt', 'salt,', 'salt to season', 'kosher salt, to taste',
                             'pinch of salt', 'onion salt', 'celery salt', 'salt, to taste', 'lbs salt', 'garlic salt',
                             'little salt', 'mediterranean sea salt', 'of salt', 'coarse salt', 'garlic salt to taste',
                             'cracked sea salt', 'salt (or more to taste)', 'salt as per taste', 'salt -',
                             'salt (to taste)']:
                recipe_info[c1]['ingredients'][c2] = u'salt'

            elif i.lower() in ['salt and pepper', u'salt &amp; pepper', 'large pinch kosher salt &amp; black pepper',
                               'salt and pepper to taste', 'salt and black pepper', u'salt&amp;pepper',
                               'salt and pepper for taste', 'sea salt and freshly ground black pepper',
                               'kosher salt &amp; black pepper', 'kosher salt and black pepper',
                               'salt &amp; pepper to taste', u'kosher salt &amp; freshly cracked black pepper',
                               'ts salt', 'salt, pepper', 'salt/pepper', 'salt pepper', 'pepper and salt',
                               'each salt and pepper', 'black pepper and salt to taste',
                               'salt, pepper, italian seasoning', 'large pinch kosher salt and black pepper',
                               'salt n pepper', 'salt and freshly ground black pepper',
                               'black pepper, and salt  to taste', 'salt pepper and', 'salt - pepper',
                               'salt and pepper (to taste)', 'of salt and pepper']:
                recipe_info[c1]['ingredients'][c2] = u'salt'
                recipe_info[c1]['ingredients'].extend([u'pepper'])

            elif i.lower() in [u'salt &amp; sugar']:
                recipe_info[c1]['ingredients'][c2] = u'salt'
                recipe_info[c1]['ingredients'].extend([u'sugar'])

            elif i.lower() in ['ground black pepper', 'fresh ground black pepper', 'fresh ground pepper',
                               'cracked black pepper', 'course black pepper', 'freshly ground black pepper',
                               'cracked pepper', 'fresh cracked black pepper', 'pepper to taste',
                               'black pepper, to taste', 'pinch of black pepper', 'black pepper to taste',
                               'coarse ground black pepper', 'fresh black pepper', 'coarse black pepper',
                               'ground pepper', 'as needed black pepper to taste', 'crushed black pepper',
                               'freshly ground pepper', 'black pepper powder', 'black pepper ground', 'pepper powder']:
                recipe_info[c1]['ingredients'][c2] = u'black pepper'

            elif i.lower() in ['crushed red pepper', 'ground red pepper', 'red pepper flakes',
                               'crushed red pepper flakes']:
                recipe_info[c1]['ingredients'][c2] = u'red pepper'

            elif i.lower() in ['ground white pepper', 'white pepper powder']:
                recipe_info[c1]['ingredients'][c2] = u'white pepper'

            elif i.lower() in ['chili', 'red chili powder', 'chile powder', 'red chilli powder', 'red chilly powder',
                               'kashmiri chilli powder']:
                recipe_info[c1]['ingredients'][c2] = u'chili powder'

            elif i.lower() in ['diced green chiles', 'green chilies', 'diced green chilies', 'can diced green chiles',
                               'can green chilies', 'green chiles', 'diced green chilis', 'green chillies',
                               'green chilli chopped', 'green chillies -', 'green chillies chopped']:
                recipe_info[c1]['ingredients'][c2] = u'green chili'

            elif i.lower() in ['diced red chiles', 'red chilies', 'diced red chilies', 'can diced red chiles',
                               'can red chilies', 'red chiles', 'diced red chilis', 'red chillies',
                               'red chilli chopped']:
                recipe_info[c1]['ingredients'][c2] = u'red chili'

            elif i.lower() in ['garlic, minced', 'minced garlic', 'granulated garlic powder', 'garlic powder',
                               'garlic cloves', 'garlic minced', 'garlic cloves, minced', 'chopped garlic',
                               'garlic clove', 'granulated garlic', 'garlic; minced', 'garlic, chopped',
                               'garlic cloves minced', 'garlic, crushed', 'garlics', 'garlic clove, sliced',
                               'garlic clove minced', 'garlic chopped', 'garlic crushed', 'garlic cloves, crushed',
                               'garlic, sliced', 'garlic (minced)', 'crushed garlic', 'garlic; creamed',
                               'garlic cloves; creamed', 'fine minced garlic', 'jarred minced garlic',
                               'fresh minced garlic', 'garlic, finely chopped', 'garlic clove, minced',
                               'fresh garlic (minced)', 'of garlic', 'fresh garlic', 'garlic (chopped)',
                               'garlic cloves chopped', 'roasted garlic', 'garlic; slivered', 'garlic diced',
                               'garlic (finely chopped)', 'garlic (grated)', 'dice garlic', 'grated garlic',
                               'garlic cloves, chopped']:
                recipe_info[c1]['ingredients'][c2] = u'garlic'

            elif i.lower() in ['bay leaves', 'crushed bay leaves', 'bayleaf', 'dried bay leaves']:
                recipe_info[c1]['ingredients'][c2] = u'bay leaf'

            elif i.lower() in ['dried thyme', 'dryed thyme']:
                recipe_info[c1]['ingredients'][c2] = u'thyme'

            elif i.lower() in ['ground ginger', 'fresh ginger', 'minced ginger', 'grated ginger', 'ginger (minced)',
                               'chopped ginger', 'fresh grated ginger', 'grind ginger', 'grated fresh ginger',
                               'ginger chopped', 'ginger root', 'ginger (finely chopped)', 'ginger, grated',
                               'fresh ginger, grated', 'fresh minced ginger']:
                recipe_info[c1]['ingredients'][c2] = u'ginger'

            elif i.lower() in ['ground cinnamon', 'cinnamon stick', 'cinnamon powder', 'cinnamon sticks',
                               'little cinnamon', 'of cinnamon']:
                recipe_info[c1]['ingredients'][c2] = u'cinnamon'

            elif i.lower() in ['ground cardamom', 'cardamom powder']:
                recipe_info[c1]['ingredients'][c2] = u'cardamon'

            elif i.lower() in ['fresh parsley', 'parsley flakes', 'chopped fresh parsley', 'chopped parsley',
                               'chopped parsley flakes', 'dry parsley', 'finely chopped parsley', 'parsley leaves',
                               'dried parsley', 'fresh chopped parsley', 'parsley, chopped', 'parsley, finely chopped',
                               'minced parsley']:
                recipe_info[c1]['ingredients'][c2] = u'parsley'

            elif i.lower() in ['fresh rosemary, minced', 'dried rosemary', 'fresh rosemary', 'minced fresh rosemary',
                               'fresh rosemary; minced', 'rosemary sprigs']:
                recipe_info[c1]['ingredients'][c2] = u'rosemary'

            elif i.lower() in ['fresh cilantro', 'cilantro, chopped', 'fresh cilantro leaves', 'chopped cilantro',
                               'chopped fresh cilantro', 'fresh cilantro, chopped', 'fresh chopped cilantro',
                               'dried cilantro', u'coriander', 'coriander powder', 'coriander ground',
                               'cilantro; chiffonade', 'cilantro chopped', 'fresh cilantro chopped',
                               'coriander sedcilantro', 'bundle cilantro; chiffonade', 'corriander',
                               'cilantro (chopped)', 'cilantro minced', 'coriander leaves', 'fresh coriander',
                               'coriander leaves chopped', 'chopped coriander']:
                recipe_info[c1]['ingredients'][c2] = u'cilantro'

            elif i.lower() in ['ground coriander seed', 'ground coriander', 'coriander powder -']:
                recipe_info[c1]['ingredients'][c2] = u'coriander seed'

            elif i.lower() in ['fresh basil', 'dried basil', 'basil leaves', 'fresh basil leaves',
                               'chopped fresh basil', 'chopped basil', 'fresh basil chopped', 'dry basil',
                               'dried basil leaves', 'fresh chopped basil', 'sweet basil', 'fresh basil (chopped)',
                               'fresh basil; chiffonade', 'chopped fresh basil leaves',
                               'fresh basil leaves, finely chopped', 'basil leaves chopped', 'dried or fresh basil',
                               'basil leaf', 'finely chopped basil', 'fresh basil leaves, chopped', 'basil dried',
                               'basil leafs', 'each chopped fresh basil, parsley chives', 'fresh basil, chopped']:
                recipe_info[c1]['ingredients'][c2] = u'basil'

            elif i.lower() in ['thai basil leaves', 'fresh thai basil']:
                recipe_info[c1]['ingredients'][c2] = u'thai basil'

            elif i.lower() in ['mexican oregano', 'whole leaf oregano', 'dried oregano', 'ground oregano',
                               'fresh oregano', 'dried oregano leaves', 'oregano dried', 'greek oregano',
                               'little oregano', 'oregano, dried', 'mexican oregeno [crushed]',
                               'mexican oregano [crushed]', 'dried mexican oregano']:
                recipe_info[c1]['ingredients'][c2] = u'oregano'

            elif i.lower() in ['dried mint', 'mint leaves', 'fresh mint', 'chopped fresh mint', 'mint leaves chopped']:
                recipe_info[c1]['ingredients'][c2] = u'mint'

            elif i.lower() in ['fresh dill', 'dill weed', 'dried dill', 'finely chopped dill',
                               'fresh dill, chopped', 'dill, finely chopped', 'fresh chopped dill']:
                recipe_info[c1]['ingredients'][c2] = u'dill'

            elif i.lower() in ['fresh thyme', 'fresh thyme; minced', 'dry thyme', 'ground thyme',
                               'chopped fresh thyme', '']:
                recipe_info[c1]['ingredients'][c2] = u'thyme'

            elif i.lower() in ['ground cumin', 'cumin powder', 'cumin seeds', 'cumin ground', 'cummin', 'cumin seed']:
                recipe_info[c1]['ingredients'][c2] = u'cumin'

            elif i.lower() in ['italian seasoning','dried italian seasoning', 'italian spices', 'italian seasonings', 'italian season',
                               'italian herbs', 'dry italian seasoning', 'italian dressing seasoning',
                               'italian seasoning spice blend']:
                recipe_info[c1]['ingredients'][c2] = u'Italian seasoning'

            elif i.lower() in ['greek seasoning', 'greek blend seasoning']:
                recipe_info[c1]['ingredients'][c2] = u'Greek seasoning'

            elif i.lower() in ['taco seasoning mix', 'taco season']:
                recipe_info[c1]['ingredients'][c2] = u'taco seasoning'

            elif i.lower() in ['ground nutmeg']:
                recipe_info[c1]['ingredients'][c2] = u'nutmeg'

            elif i.lower() in ['turmeric powder', 'ground turmeric', 'tumeric', 'tumeric powder', 'turmeric powder -']:
                recipe_info[c1]['ingredients'][c2] = u'turmeric'

            elif i.lower() in ['curry leaves', 'curry leaves -', 'curry leaves few',
                               'curry leaves or coriander leaves']:
                recipe_info[c1]['ingredients'][c2] = u'curry leaf'

            elif i.lower() in ['cayenne', 'cayenne powder', 'ground cayenne pepper']:
                recipe_info[c1]['ingredients'][c2] = u'cayenne pepper'

            elif i.lower() in ['ground allspice']:
                recipe_info[c1]['ingredients'][c2] = u'allspice'

            elif i.lower() in ['crayfish 2 tbs(blended)', 'cup crayfish', 'table spoon of crayfish blended',
                               'full teaspoon crayfish (blended)', 'crayfish(blended)',
                               'table spoon crayfish (blended)', 'grounded crayfish',
                               'full teaspoon of blended crayfish', 'medium crayfish (blended)',
                               'crayfish picked and washed (as you want)',
                               'fresh live crayfish (crafish/ crawdads) yields about 1 cup',
                               'table spoon blended crayfish', 'crayfish blended', 'spoon crayfish (blended)',
                               'table spoon crayfish', 'table spoon of crayfish', 'blended crayfish',
                               'crayfish (blended)']:
                recipe_info[c1]['ingredients'][c2] = u'crayfish'

            elif i.lower() in ['ground cloves', 'whole cloves']:
                recipe_info[c1]['ingredients'][c2] = u'cloves'

            elif i.lower() in ['vegetable broth', 'stock']:
                recipe_info[c1]['ingredients'][c2] = u'vegetable stock'

            elif i.lower() in ['chicken broth', 'chicken flavor bouillon', 'chicken bouillon', 'chicken bullion',
                               'chicken bouillon cubes', 'water or chicken stock', 'chicken stock powder',
                               'spoon of chicken stock powder', 'of chicken stock']:
                recipe_info[c1]['ingredients'][c2] = u'chicken stock'

            elif i.lower() in ['beef broth', 'beef bouillon cubes']:
                recipe_info[c1]['ingredients'][c2] = u'beef stock'

            elif i.lower() in ['vanilla', 'pure vanilla extract', 'vanilla essence', ]:
                recipe_info[c1]['ingredients'][c2] = u'vanilla extract'

            elif i.lower() in ['of sugar', 'spoon of sugar']:
                recipe_info[c1]['ingredients'][c2] = u'sugar'

            elif i.lower() in ['garam masala -']:
                recipe_info[c1]['ingredients'][c2] = u'garam masala'

            # SAUCES

            elif i.lower() in ['worchestershire sauce', 'worcestershire', 'worcester sauce', 'worshestershire sauce',
                               'worceshire sauce', 'worshire sauce', 'worchestire sauce',
                               'as needed dales or worchershire sauce']:
                recipe_info[c1]['ingredients'][c2] = u'worcestershire sauce'

            elif i.lower() in ['light soy sauce', 'dark soy sauce', 'low sodium soy sauce', 'sweet soy sauce',
                               'tamari soy sauce', 'low-sodium soy sauce', 'soysauce']:
                recipe_info[c1]['ingredients'][c2] = u'soy sauce'

            elif i.lower() in ['boiling water', 'cold water', 'warm water', 'water divided', 'water or chicken broth',
                               'water or broth', 'water warm', 'some water', 'water as needed', 'hot water',
                               'ice water', 'of water', 'water -']:
                recipe_info[c1]['ingredients'][c2] = u'water'

            elif i.lower() in ['ice cubes']:
                recipe_info[c1]['ingredients'][c2] = u'ice'

            elif i.lower() in ['tahini paste', 'tahini (sesame paste)', 'tahina']:
                recipe_info[c1]['ingredients'][c2] = u'tahini'

            elif i.lower() in ['white vinegar', 'vinegar', 'distilled white vinegar']:
                recipe_info[c1]['ingredients'][c2] = u'white wine vinegar'

            elif i.lower() in ['cider vinegar']:
                recipe_info[c1]['ingredients'][c2] = u'apple cider vinegar'

            elif i.lower() in ['cream of chicken', 'can cream of chicken']:
                recipe_info[c1]['ingredients'][c2] = u'cream of chicken soup'

            elif i.lower() in ['cream of mushroom']:
                recipe_info[c1]['ingredients'][c2] = u'cream of mushroom soup'

            elif i.lower() in ['mild salsa', 'medium salsa', 'red salsa', 'salsa (optional)']:
                recipe_info[c1]['ingredients'][c2] = u'salsa sauce'

            elif i.lower() in ['can enchilada sauce']:
                recipe_info[c1]['ingredients'][c2] = u'enchilada sauce'

            elif i.lower() in ['sriracha', 'sriracha hot sauce']:
                recipe_info[c1]['ingredients'][c2] = u'sriracha sauce'

            elif i.lower() in ['quality fish sauce', 'fishsauce', 'spoon of fish sauce', 'of fish sauce']:
                recipe_info[c1]['ingredients'][c2] = u'fish sauce'

            elif i.lower() in ['creamy peanut butter']:
                recipe_info[c1]['ingredients'][c2] = u'peanut butter'

            # OILS/FATS

            elif i.lower() in ['extra virgin olive oil', 'olive oil, extra virgin', 'olive oil, i used chili infused',
                               'extra-virgin olive oil', 'olive oil, divided', 'as needed olive oil',
                               'virgin olive oil', 'olive oil extra virgin', 'evoo', 'garlic olive oil']:
                recipe_info[c1]['ingredients'][c2] = u'olive oil'

            elif i.lower() in ['oil', 'vegetable oil; as needed', 'vegetable oil', 'oil for frying',
                               'vegetable oil for frying', 'veg oil', 'frying oil', 'vegetable or olive oil',
                               'sesame or vegetable oil', 'oil for deep frying', 'oil to fry', 'oil -',
                               'cooking oil (shallow frying)', 'oil   for   deep   frying']:
                recipe_info[c1]['ingredients'][c2] = u'cooking oil'

            elif i.lower() in ['sesame oil (optional)', 'sesame seed oil', 'toasted sesame oil']:
                recipe_info[c1]['ingredients'][c2] = u'sesame oil'

            elif i.lower() in ['nonstick cooking spray']:
                recipe_info[c1]['ingredients'][c2] = u'cooking spray'

            elif i.lower() in ['unsalted butter', 'melted butter', 'butter, melted', 'butter (melted)',
                               'butter; melted', 'butter or margarine', 'butter, softened', 'butter melted',
                               'of butter', 'softened butter', 'butter- softened', 'salted butter']:
                recipe_info[c1]['ingredients'][c2] = u'butter'

            # CARBS

            elif i.lower() in ['all purpose flour', 'all-purpose flour', 'plain flour', 'sr flour', 'bread flour',
                               'ap flour', 'wheat flour', 'cake flour', 'whole wheat flour']:
                recipe_info[c1]['ingredients'][c2] = u'flour'

            elif i.lower() in ['cooked rice', 'long grain rice', 'white rice', 'cooked white rice',
                               'long grain white rice', 'uncooked rice', 'instant rice', 'medium grain rice',
                               'minute rice', 'rice cooked', 'steamed rice']:
                recipe_info[c1]['ingredients'][c2] = u'rice'

            elif i.lower() in ['potatoes', 'large potatoes', 'potatos', 'russet potatoes', 'baby potatoes',
                               'potatoes (cubed)', 'small peeled potatoes', 'potatoes, cubed', 'diced potatoes',
                               'mashed potatoes', 'large russet potatoes', 'boiled potatoes']:
                recipe_info[c1]['ingredients'][c2] = u'potato'

            elif i.lower() in ['sweet potatoes']:
                recipe_info[c1]['ingredients'][c2] = u'sweet potato'

            elif i.lower() in ['breadcrumbs', 'dry bread crumbs', 'italian bread crumbs', 'italian breadcrumbs',
                               'panko bread crumbs', 'panko breadcrumbs', 'seasoned bread crumbs',
                               'plain bread crumbs', 'italian style bread crumbs', 'italian seasoned bread crumbs',
                               'italian style breadcrumbs']:
                recipe_info[c1]['ingredients'][c2] = u'bread crumbs'

            elif i.lower() in ['french bread', 'italian bread', 'ciabatta bread', 'white bread', 'pita bread']:
                recipe_info[c1]['ingredients'][c2] = u'bread'

            elif i.lower() in ['flour tortillas', 'corn tortillas', 'white corn tortillas', 'large flour tortillas',
                               'large flour tortillas (microwave 30 seconds)', 'warm flour tortillas', 'tortilla',
                               'fresh flour tortillas', 'flour or corn tortillas', 'soft corn tortillas',
                               'yellow corn tortillas', 'flour tortilla', 'small flour tortillas', 'corn tortilla',
                               'large tortillas', 'small tortillas', 'soft tortillas', 'corn or flour tortillas',
                               'of tortillas', u'6&quot; flour tortillas', 'soft taco size flour tortillas',
                               'whole wheat tortillas', 'warmed tortillas']:
                recipe_info[c1]['ingredients'][c2] = u'tortillas'

            elif i.lower() in ['wide egg noodles']:
                recipe_info[c1]['ingredients'][c2] = u'egg noodles'

            elif i.lower() in ['spaghetti noodles', 'spaghetti pasta', 'dry spaghetti', 'thin spaghetti',
                               'italian spaghetti', 'enriched spaghetti pasta', 'dry spaghetti pasta']:
                recipe_info[c1]['ingredients'][c2] = u'spaghetti'

            elif i.lower() in ['rolled oats', 'old fashioned oats']:
                recipe_info[c1]['ingredients'][c2] = u'oats'

            elif i.lower() in ['sliced almonds', 'blanched almonds', 'raw almonds']:
                recipe_info[c1]['ingredients'][c2] = u'almonds'

            elif i.lower() in ['sesame', 'toasted sesame seeds', 'roasted sesame seeds', 'white sesame seeds']:
                recipe_info[c1]['ingredients'][c2] = u'sesame seeds'

            # VEG

            elif i.lower() in ['onions', 'onion, chopped', 'onion powder', 'chopped onion', 'onion, diced',
                               'onion chopped', 'large onion', 'small onion', 'medium onion', 'diced onion',
                               'chopped onions', 'small onion, chopped', 'medium onion chopped', 'minced onion',
                               'medium onion, chopped', 'onion diced', 'onion (chopped)', 'medium size onion',
                               'onions, diced', 'large onion chopped', 'chop onions', 'small onion finely chopped',
                               'onions, sliced', 'large onion, chopped', 'onion, minced', 'small onion diced',
                               'small diced onion', 'onion sliced', 'medium onion diced', 'onion, sliced',
                               'finely chopped onion', 'diced onions', 'medium bulb onion', 'onion medium sized',
                               'onion, finely chopped', 'onion ,peeled and very finely diced', 'onions, chopped',
                               'onion (diced)', 'onion finely chopped', 'large onions', 'sliced onion',
                               'medium onions', 'graded onion', 'medium onion, diced', 'onions chopped',
                               'onion, thinly sliced', 'onions sliced']:
                recipe_info[c1]['ingredients'][c2] = u'onion'

            elif i.lower() in ['green onions, chopped', 'green onions', 'green onions, sliced', 'chopped green onion',
                               'green onions chopped', 'sliced green onions', 'chopped green onions',
                               'minced green onion', 'green onion (chopped)']:
                recipe_info[c1]['ingredients'][c2] = u'green onion'

            elif i.lower() in ['yellow onion, chopped', 'chopped yellow onion', 'yellow onion; minced',
                               'diced yellow onion']:
                recipe_info[c1]['ingredients'][c2] = u'yellow onion'

            elif i.lower() in ['red onion, chopped', 'chopped red onion', 'red onion, diced',
                               'finely chopped red onion', 'red onion, finely chopped', 'red onion; minced',
                               'diced red onion', 'red onion diced', 'red onion; small dice',
                               'small red onion; small dice', 'red onion (diced)', 'red onions']:
                recipe_info[c1]['ingredients'][c2] = u'red onion'

            elif i.lower() in ['white onions', 'white onion chopped', 'diced white onion', 'white onion, diced',
                               'large white onion', 'white onion diced']:
                recipe_info[c1]['ingredients'][c2] = u'white onion'

            elif i.lower() in ['spring onions']:
                recipe_info[c1]['ingredients'][c2] = u'spring onion'

            elif i.lower() in ['shallots', 'small shallots']:
                recipe_info[c1]['ingredients'][c2] = u'shallot'

            elif i.lower() in [u'scallions']:
                recipe_info[c1]['ingredients'][c2] = u'scallion'

            elif i.lower() in ['chopped chives', 'dried chives', 'finely chopped chives', 'chives/green onions',
                               'chopped asian chives', 'chives', 'fresh chives']:
                recipe_info[c1]['ingredients'][c2] = u'chives'

            elif i.lower() in ['carrots', 'baby carrots', 'large carrots', 'chopped carrots', 'carrots diced',
                               'carrots, chopped', 'shredded carrots', 'medium carrots', 'carrots chopped',
                               'carrots, sliced', 'grated carrot', 'shredded carrot', 'carrots, shredded',
                               'small carrot']:
                recipe_info[c1]['ingredients'][c2] = u'carrot'

            elif i.lower() in ['diced tomatoes', 'large tomatoes', 'chopped tomatoes', 'cherry tomatoes', 'tomatoes',
                               'roma tomatoes, diced', 'ripe tomatoes', 'roma tomatoes', 'rotel tomatoes',
                               'tomatoes chopped', 'medium tomatoes', 'large tomato', 'small tomato',
                               'crushed tomatoes', 'stewed tomatoes', 'diced tomatos', 'tomatoe',
                               'cherry tomatoes, halved', 'tomato, chopped', 'tomato diced', 'grape tomatoes',
                               'plum tomatoes', u'chopped tomato', 'roma tomato', 'tomatos', 'tomato chopped',
                               'diced tomato', 'tomatoes diced', 'tomato, diced', 'tomatoes, diced',
                               'diced tomatoes, undrained', 'diced tomatoe', 'fire roasted diced tomatoes',
                               'can diced tomatoes', 'roma tomatoes, chopped', 'tomato (chopped)']:
                recipe_info[c1]['ingredients'][c2] = u'tomato'

            elif i.lower() in ['can of tomato sauce', 'can tomato sauce', 'tomatoe sauce']:
                recipe_info[c1]['ingredients'][c2] = u'tomato sauce'

            elif i.lower() in ['sliced mushrooms', 'mushrooms', 'mushrooms, sliced', 'fresh mushrooms',
                               'canned mushrooms, drained', 'fresh sliced mushrooms', 'chopped mushrooms']:
                recipe_info[c1]['ingredients'][c2] = u'mushroom'

            elif i.lower() in ['shiitake mushrooms', 'dried shiitake mushroom']:
                recipe_info[c1]['ingredients'][c2] = u'shiitake mushroom'

            elif i.lower() in ['celery chopped', 'chopped celery', 'sliced celery', 'stalks of celery',
                               'celery, sliced', 'celery, diced', 'celery, chopped', 'celery stalks', 'diced celery',
                               'finely chopped celery']:
                recipe_info[c1]['ingredients'][c2] = u'celery'

            elif i.lower() in ['frozen broccoli', 'frozen broccoli florets', 'chopped broccoli', 'broccoli florets',
                               'fresh broccoli', 'broccoli, bite size', 'brocoli']:
                recipe_info[c1]['ingredients'][c2] = u'broccoli'

            elif i.lower() in ['green pepper', 'chopped green bell pepper', 'green bell pepper, diced',
                               'green bell peppers', 'green bell pepper, chopped', 'green pepper, chopped',
                               'green pepper, diced', 'green peppers', 'chopped green pepper', 'green pepper chopped',
                               'green bell pepper, sliced']:
                recipe_info[c1]['ingredients'][c2] = u'green bell pepper'

            elif i.lower() in ['red pepper', 'chopped red bell pepper', 'red bell pepper, diced',
                               'red bell peppers', 'red bell pepper, chopped', 'red pepper, chopped',
                               'red pepper, diced', 'red peppers', 'chopped red pepper', 'red bell pepper, chopped',
                               'red bell pepper; medium dice', 'red bell pepper, sliced',
                               'red bell pepper; small dice']:
                recipe_info[c1]['ingredients'][c2] = u'red bell pepper'

            elif i.lower() in ['bell peppers', 'bell pepper, chopped', 'bell pepper, diced', 'bell pepper chopped',
                               'peppers', 'chopped bell pepper', 'small bell pepper, diced']:
                recipe_info[c1]['ingredients'][c2] = u'bell pepper'

            elif i.lower() in ['fresh lemon juice', 'juice of 1 lemon', 'lemon extract',
                               'lemon juice from whole lemon',
                               'juice of one lemon', 'lemon, juiced', 'reallemon juice',
                               'freshly squeezed lemon juice', 'juice of lemon', 'lemon juiced', 'juice of 2 lemons',
                               'lemons, juiced', 'juice of half a lemon']:
                recipe_info[c1]['ingredients'][c2] = u'lemon juice'

            elif i.lower() in ['fresh lime juice', 'juice of 1 lime', 'lime extract',
                               'lime juice from whole lime', 'juice of one lime', 'lime, juiced',
                               'freshly squeezed lime juice', 'juice of lime', 'lime juiced', 'juice of 2 limes',
                               'limes, juiced', 'juice of half a lime', 'limes juiced', 'lime; juiced',
                               'lime juiced', 'freshly squeezed lime juice', 'limes (juiced)']:
                recipe_info[c1]['ingredients'][c2] = u'lime juice'

            elif i.lower() in ['limes', 'lime zest', 'lime wedges', 'fresh lime']:
                recipe_info[c1]['ingredients'][c2] = u'lime'

            elif i.lower() in ['lemon wegdes', 'lemons']:
                recipe_info[c1]['ingredients'][c2] = u'lemon'

            elif i.lower() in ['ripe banana', 'bananas', 'frozen banana', 'ripe bananas']:
                recipe_info[c1]['ingredients'][c2] = u'banana'

            elif i.lower() in ['pumpkin puree']:
                recipe_info[c1]['ingredients'][c2] = u'pumpkin'

            elif i.lower() in ['frozen corn', 'corn, drained', 'of corn', 'whole kernel corn', 'sweet corn', 'corn',
                               'corn (drained)', 'whole kernel corn, drained', 'corn kernels']:
                recipe_info[c1]['ingredients'][c2] = u'sweetcorn'

            elif i.lower() in ['frozen spinach', 'baby spinach', 'fresh baby spinach', 'fresh spinach',
                               'chopped spinach', 'fresh spinach, chopped', 'baby spinach leaves', 'of spinach',
                               'packed baby spinach fresh', 'bunch fresh baby spinach leaves', 'spinach leaves',
                               'frozen chopped spinach', 'spinich', 'boiled spinach']:
                recipe_info[c1]['ingredients'][c2] = u'spinach'

            elif i.lower() in ['eggplant', 'eggplants', 'eggplant, sliced',
                               'eggplant,  peeled and sliced the longway into 1/4 inch slices']:
                recipe_info[c1]['ingredients'][c2] = u'aubergine'

            elif i.lower() in ['zucchini']:
                recipe_info[c1]['ingredients'][c2] = u'courgette'

            elif i.lower() in ['black olives', 'sliced black olives', 'sliced olives', 'olives',
                               'sliced black olives (optional)']:
                recipe_info[c1]['ingredients'][c2] = u'black olive'

            elif i.lower() in ['kalamata olives', 'Kalamata olives', 'Kalamata olive', 'pitted kalamata olives',
                               'sliced kalamata olives']:
                recipe_info[c1]['ingredients'][c2] = u'kalamata olive'

            elif i.lower() in ['cucumbers', 'cucumber, chopped', 'sliced cucumber', 'chopped cucumber']:
                recipe_info[c1]['ingredients'][c2] = u'cucumber'

            elif i.lower() in ['shredded lettuce', 'chopped lettuce', 'iceberg lettuce', 'lettuce, shredded',
                               'lettuce, chopped', 'letuce']:
                recipe_info[c1]['ingredients'][c2] = u'lettuce'

            elif i.lower() in ['shredded cabbage']:
                recipe_info[c1]['ingredients'][c2] = u'cabbage'

            elif i.lower() in [u'jalape\xf1o', u'jalape\xf1os', u'jalapenos', u'jalape\xf1o peppers', u'jalape\xf1o pepper',
                               u'sliced jalape\xf1os', u'jalape\xf1o (optional)', u'jalape\xf1os; small dice',
                               u'jalape\xf1o chopped', u'jalapeno peppers', u'jalape\xf1o pepper, diced',
                               u'jalape\xf1o peppers, chopped', u'jalapeno pepper (optional)', u'jalape\xf1o (diced)',
                               u'jalape\xf1o minced', u'jalape\xf1os; minced', u'jalapeno pepper',
                               u'jalape\xf1o seeded &amp; ribs removed', u'jalepeno']:
                recipe_info[c1]['ingredients'][c2] = u'jalapeno'

            elif i.lower() in [u'avocados', u'avacados', u'avocadoes', 'ripe avacados', 'ripe avocados',
                               'avocado, diced', 'avocadoes', 'large avocados', 'avocados diced', 'avocado; diced',
                               'ripe avocado', 'diced avocado', 'small avocados', 'avocado cut into small chunks']:
                recipe_info[c1]['ingredients'][c2] = u'avocado'

            elif i.lower() in [u'red kidney beans', u'kidney beans, drained', 'kidney beans drained']:
                recipe_info[c1]['ingredients'][c2] = u'kidney beans'

            elif i.lower() in [u'black beans, drained', u'black beans, drained and rinsed',
                               u'black beans, drained rinsed', 'black beans drained']:
                recipe_info[c1]['ingredients'][c2] = u'black beans'

            elif i.lower() in [u'can refried beans']:
                recipe_info[c1]['ingredients'][c2] = u'refried beans'

            elif i.lower() in [u'coconut grated', 'grated coconut']:
                recipe_info[c1]['ingredients'][c2] = u'coconut'

            #FRUIT

            elif i.lower() in ['frozen strawberries', 'fresh strawberries']:
                recipe_info[c1]['ingredients'][c2] = u'strawberry'

            elif i.lower() in ['fresh blueberries', 'blueberries']:
                recipe_info[c1]['ingredients'][c2] = u'blueberry'

            elif i.lower() in ['frozen pineapple']:
                recipe_info[c1]['ingredients'][c2] = u'pineapple'

            # PROTEIN

            elif i.lower() in ['eggs', 'large eggs', 'eggs, beaten', 'eggs beaten', 'each egg', 'large egg',
                               'egg yolks', 'egg whites', 'egg, beaten', 'egg yolk', 'eggs, lightly beaten',
                               'egg, lightly beaten', 'large egg yolks', 'egg wash', 'egg white',
                               'egg, slightly beaten', 'eggs (beaten)', 'raw egg', 'egg beaten', 'large eggs, beaten',
                               'egg whites (approx)', 'whole eggs', 'eggs whisked', 'egg whites (beaten)',
                               'eggs (whisked)', 'boiled eggs']:
                recipe_info[c1]['ingredients'][c2] = u'egg'

            elif i.lower() in ['grated parmesan cheese', 'grated parmesan', 'parmesan', 'shredded parmesan cheese',
                               'parmesan cheese shredded', 'freshly grated parmesan cheese',
                               'grated parmesan cheese, divided', 'parmesan cheese, grated', 'grated parmesean',
                               'shredded parmesan', 'fresh grated parmesan cheese', 'grated parmesean cheese']:
                recipe_info[c1]['ingredients'][c2] = u'parmesan cheese'

            elif i.lower() in ['shredded cheddar cheese', 'sharp cheddar cheese', 'shredded cheddar',
                               'sharp cheddar cheese, shredded', 'shredded extra sharp cheddar cheese',
                               'cheddar cheese, grated', 'cheddar cheese, shredded', 'finely shredded cheddar cheese',
                               'cheddar cheese- shredded', 'cheddar cheese shredded', 'grated chedder cheese',
                               'mild cheddar cheese', 'sharp cheddar cheese shredded',
                               'extra sharp cheddar cheese shredded', 'shredded chedder cheese',
                               'extra sharp cheddar cheese', 'grated cheddar cheese', 'cheddar cheese; shredded',
                               'shredded sharp cheddar cheese', 'shredded sharp cheddar']:
                recipe_info[c1]['ingredients'][c2] = u'cheddar cheese'

            elif i.lower() in ['shredded mozzarella cheese', 'mozzarella', 'shredded mozzarella',
                               'mozzarella cheese, shredded', 'mozzarella cheese shredded', 'grated mozzarella cheese',
                               'shredded mozzarella cheese, divided', 'fresh mozzarella', 'grated mozzarella']:
                recipe_info[c1]['ingredients'][c2] = u'mozzarella cheese'

            elif i.lower() in ['fresh grated romano cheese']:
                recipe_info[c1]['ingredients'][c2] = u'romano cheese'

            elif i.lower() in ['crumbled feta cheese', 'feta cheese, crumbled', 'feta', 'greek feta', 'cumbled feta',
                               'feta cheese crumbled']:
                recipe_info[c1]['ingredients'][c2] = u'feta cheese'

            elif i.lower() in ['shredded mexican cheese', 'mexican shredded cheese', 'mexican blend cheese',
                               'mexican 3 cheese', 'shredded mexican blend cheese', 'mexican cheese blend',
                               'shredded mexican cheese blend', 'shredded mexican style cheese',
                               'of shredded mexican blend cheese']:
                recipe_info[c1]['ingredients'][c2] = u'mexican cheese'

            elif i.lower() in ['shredded monterey jack cheese', 'monterey jack cheese, shredded',
                               'shredded cheddar jack cheese', 'monterey jack', 'pepper jack cheese, shredded',
                               'jack cheese, shredded']:
                recipe_info[c1]['ingredients'][c2] = u'monterey jack cheese'

            elif i.lower() in ['shredded pepper jack cheese']:
                recipe_info[c1]['ingredients'][c2] = u'pepper jack cheese'

            elif i.lower() in ['shredded colby jack cheese']:
                recipe_info[c1]['ingredients'][c2] = u'colby jack cheese'

            elif i.lower() in ['cream cheese, softened']:
                recipe_info[c1]['ingredients'][c2] = u'cream cheese'

            elif i.lower() in ['shredded cheese', 'grated cheese', 'shredded cheese (your choice)',
                               'cheese of your choice', 'shredded cheese of your choice', 'cheese (grated)',
                               'heavy whipping cream, cold', 'or more shredded cheese', 'sliced cheese']:
                recipe_info[c1]['ingredients'][c2] = u'cheese'

            elif i.lower() in ['evaporated milk', 'whole milk', 'can of evaporated milk', 'fresh milk', 'warm milk',
                               '2% milk']:
                recipe_info[c1]['ingredients'][c2] = u'milk'

            elif i.lower() in ['unsweetened almond milk']:
                recipe_info[c1]['ingredients'][c2] = u'almond milk'

            elif i.lower() in ['heavy whipping cream', 'heavy cream', 'whipped cream', 'whip cream',
                               'double cream (thick cream)', 'fresh cream (35% milk fat)', 'double cream', ]:
                recipe_info[c1]['ingredients'][c2] = u'whipping cream'

            elif i.lower() in ['sour cream (optional)', 'light sour cream', 'sour cream for garnish']:
                recipe_info[c1]['ingredients'][c2] = u'sour cream'

            elif i.lower() in ['mayo', 'mayonaise']:
                recipe_info[c1]['ingredients'][c2] = u'mayonnaise'

            elif i.lower() in ['plain greek yogurt', 'greek yoghurt', 'nonfat greek yogurt', 'fat free greek yogurt',
                               'plain greek yoghurt', 'sour cream or greek yogurt', 'greek yogurt plain',
                               'greek yogurt, plain', 'low fat greek yogurt', 'nonfat plain greek yogurt',
                               'non-fat greek yogurt', 'plain non fat greek yogurt', 'greek plain yogurt',
                               'plain nonfat greek yogurt', 'greek yogurt (plain or vanilla)']:
                recipe_info[c1]['ingredients'][c2] = u'Greek yogurt'

            elif i.lower() in ['plain yogurt', 'yoghurt', 'nonfat yogurt']:
                recipe_info[c1]['ingredients'][c2] = u'yogurt'

            elif i.lower() in ['plain vanilla yogurt', 'vanilla yoghurt', 'nonfat vanilla yogurt',
                               'vanilla greek yogurt', 'greek vanilla yogurt', 'vanilla nonfat greek yogurt']:
                recipe_info[c1]['ingredients'][c2] = u'vanilla yogurt'

            # MEAT

            elif i.lower() in ['chicken breasts', 'boneless chicken breasts', 'large chicken breasts',
                               'boneless chicken breast', 'boneless, skinless chicken breasts',
                               'boneless skinless chicken breasts', 'chicken breasts, boneless, skinless',
                               'boneless skinless chicken breast', 'skinless chicken breasts',
                               'skinless boneless chicken breast']:
                recipe_info[c1]['ingredients'][c2] = u'chicken breast'

            elif i.lower() in ['shredded chicken']:
                recipe_info[c1]['ingredients'][c2] = u'ground chicken'

            elif i.lower() in ['bacon bits', 'chopped bacon', 'bacon, chopped', 'bacon, diced', 'bacon; small dice',
                               ]:
                recipe_info[c1]['ingredients'][c2] = u'bacon'

            elif i.lower() in ['hamburger meat', 'hamburger', 'ground beef', 'beef mince', 'lean ground beef',
                               'ground meat', 'ground beef or turkey', 'ground beef', 'ground beef or ground turkey',
                               'ground turkey or beef']:
                recipe_info[c1]['ingredients'][c2] = u'minced beef'

            # FISH

            # NON-INGREDIENTS

            elif i.lower() in ['ingredients', 'filling', 'half and half', 'wet ingredients', 'dry ingredients', 'main',
                               'other', 'dressing', 'for the filling', 'crust', 'main ingredients', 'for the sauce',
                               'toppings', 'optional', 'optional toppings', u'\u25cf for the sides',
                               'for the toppings', 'vegetables', 'sauce', 'veggies', 'frying;']:
                del recipe_info[c1]['ingredients'][c2]

            # OTHER

            elif i.lower() in ['active dry yeast', 'instant yeast', 'rapid rise yeast', 'dry yeast',
                               'active dry yeast (use 1 tbsp instant yeast)', '(/4 oz) pkg active dry yeast']:
                recipe_info[c1]['ingredients'][c2] = u'yeast'



    return recipe_info
