# Project in Python by Emil, Lasse, Xu og Menja

## Read the Project_description.docx for all the details about the project

### Dataset is from this site: 

#### http://archive.stats.govt.nz/tools_and_services/releases_csv_files/csv-files-for-infoshare.aspx


#### We have used the dataset: Food Price Index: March 2018


### Download dataset:

#### https://raw.githubusercontent.com/menjaw/Python_Project/master/food-price-index-mar18-weighted-average-prices-csv-tables.csv.tsv 

### Dependencies & Info

The following dependencies should be installed on your system, either via conda install of pip install through your terminal:

- pandas
- pygal
- Flask
- webget(this dependenty can you get after you clone the project)

## Getting started:

### 1: run requirements.txt 
- python -r requirements.txt

### 2: run program from terminal:
- python run.py

## Dataset 1 (weighted-average-prices)
#### Question 1
- How many products have been tested?
##### Answer: 148 products has been tested
#### Question 2
- How many times have each product been tested?


##### Answer: 
| Product					     | Amount   |
|:--------------------------------------------------:|:--------:|
| Apples, 1kg                                        |   142    |
| Apricots, dried, 100g                              |     81   |
| Avocado, 1kg                                       |    134|
| Baby food, 110g                                    |    134|
| Bacon - middle rashers (supermarket only), 700g    |     46|
| Bananas, 1kg                                          | 142|
| Beans, 1kg                                            | 134|
| Beef - mince, 1kg                                     | 142|
| Beef steak - blade, 1kg                               | 142|
| Beef steak - porterhouse/sirloin, 1kg                 | 142|
| Berries, frozen, 500g                                 |  81|
| Biscuits - chocolate, 200g                            | 142|
| Biscuits, plain (eg arrowroot, ginger, malt, wi...    | 134|
| Biscuits, savoury, crackers 250g                      | 134|
| Bottled water, 750ml                                  | 142|
| Bread - white sliced loaf, 600g                       | 142|
| Bread rolls, filled, hot, each                        | 134|
| Bread rolls, hamburger buns, 6 pack                   | 134|
| Breakfast biscuits, 1kg                               | 142|
| Breakfast drink, 250ml, 6 pack                        |  45|
| Broccoli, 1kg                                         | 142|
| Burger, with or without accompaniments, each          | 134|
| Butter - salted, 500g                                 | 142|
| Cabbage, 1kg                                          | 142|
| Cakes and biscuits, takeaway                          | 134|
| Capsicums, green, else red, 1kg                       | 134|
| Carrots, 1kg                                           |142|
| Cauliflower, 1kg                                       |134|
| Celery, 1kg                                           | 134|
|Cheese - mild cheddar (supermarket only), 1kg          |142|
|Cheese, camembert, 125g                                |134|
|Cheese, processed slices, 250g                         |134|
|Chicken breast, 1kg                                     |46|
|Chicken nuggets, frozen, 1kg                            |81|
|Chicken pieces (excluding breast), boneless or ...      |45|
|Chicken, cooked, whole, No. 15 - Cheapest Avail...     |117|
|Chicken, whole, frozen, No. 15 - Cheapest Avail...     |134|
|Chilled fruit juice or smoothies, 1 to 1.5 litre       |117|
|Chocolate - block (supermarket only), 250g            | 142|
|Chocolate blocks, convenience stores, 100g to 250g     |134|
|Chocolate novelty bars, 50g                            |134|
|Chocolate, boxed, loose, 250g                          |134|
|Coffee - instant, 100g                                | 142|
|Coffee, ground, 200g                                   |134|
|Coffee, takeway, each                                 |134|
|Cookie, takeaway, each                                | 134|
|Corn flakes, 500g                                      |134|
|Corned beef, fresh, chilled or frozen, 1kg            | 134|
|Courgettes, 1kg                                       | 134|
|Cream, 300ml - Cheapest Available                     | 134|
|Cucumber, 1kg                                         | 134|
|Dessert, frozen, 500g                                 | 117|
|Dried pasta, spaghetti or other type, 500g             |117|
|Drinking chocolate, 300g                               |134|
|Eggs, dozen                                           | 142|
|Eggs, free range, 6 pack                              | 117|
|Fish and chips, One fish/chips                         |142|
|Fish fillets, frozen, multipack, 500g                 | 134|
|Flat bread - pita, tortilla, or other type             | 81|
|Flour - white (supermarket only), 1.5kg               | 142|
|Fresh fish, 1kg                                        |134|
|Fresh herbs, packaged, chilled                          | 6|
|Fresh pasta, tortellini or other filled type, 300g    | 117|
|Fried and other takeaway chicken, 5 pieces             |134|
|Fruit flavoured drink powder, multipack of 3 to 5     | 134|
|Fruit juice - apple based (supermarket only), 3...     | 82|
|Grapes, green or red                                  | 134|
|Honey, clover, creamed, 500g                          | 134|
|Hot chips, hot wedges                                 | 134|
|Hummus dip, 200g                                       |117|
|Ice block, water based, each                          | 134|
|Ice cream bought in bulk, 2 litres                    | 134|
|Ice cream novelty, chocolate coated, each              |134|
|Infant formula, 900g                                  | 134|
|Jam, 375g                                             | 134|
|Kiwifruit, 1kg                                        | 142|
|Kumara, 1kg                                           | 134|
|Lamb - chops, 1kg                                     | 142|
|Lettuce, 1kg                                          | 142|
|Mandarins, 1kg                                        | 134|
|Meat pie - hot, each                                  | 142|
|Meat pies, chilled, 6 or 8 pack - Cheapest Avai...    | 134|
|Milk - standard homogenised, 2 litres                 | 142|
|Milk, calcium enriched, 2 litres                       |134|
|Mixed vegetables, frozen, 1kg                         | 134|
|Muesli, natural or toasted, 750g                      | 134|
|Muesli/cereal bars, 200g                              | 117|
|Mushrooms, 1kg                                        | 142|
|Mussels, live, 1kg                                    | 134|
|Mussels, marinated, 375g                              | 134|
|Olive oil, pure, not extra virgin or light, 1 l...    | 134|
|Olives, jar, 400g                                      |  6|
|Onions, 1kg                                           | 134|
|Orange juice, not apple based, 1 litre - Cheape...    |  81|
|Oranges, 1kg                                          | 142|
|Packaged cake slice, 300g                             | 134|
|Packaged meal, pasta and sauce, 130g                   |134|
|Parsnips, 1kg                                         | 134|
|Pasta sauces, tomato based, 500g                      | 134|
|Pastry, frozen sheets, puff or flaky, 800g            | 134|
|Peaches - canned (supermarket only), 410g             | 142|
|Peanut butter, not salt free, 375g                   |  142|
|Pears, 1kg                                            | 134|
|Peas - frozen (supermarket only), 1kg                 | 142|
|Pineapple, 1kg                                        | 117|
|Pineapple, pieces, in juice or syrup, canned, 425g     |134|
|Pizza, takeaway                                       | 134|
|Pork - loin chops, 1kg                                | 142|
|Potato crisps, 150g                                    | 82|
|Potato fries, frozen, 1kg                             | 134|
|Potatoes, 1kg                                         | 142|
|Prawns, frozen, 700g                                   | 45|
|Prepared meals, frozen, 340g                          | 134|
|Pumpkin, 1kg                                          | 134|
|Rice - long grain, white (supermarket only), 1kg      | 142|
|Roasting lamb and hogget, fresh, chilled or fro...    | 134|
|Roasting pork, fresh, chilled or frozen, 1kg          | 134|
|Salad, leaf, packaged, 150g                           |  45|
|Salad, takeaway, vegetable, 1kg                       | 134|
|Salami, 100g                                          | 134|
|Salmon, imported, pink, canned, unflavoured, 210g     | 134|
|Sandwich, fresh or toasted                           |  142|
|Sausages, 1kg                                         | 142|
|Soft drink, 1.5 litres                                | 142|
|Soft drinks, 600ml                                    | 134|
|Soft drinks, poured                                    |134|
|Soup, canned, 500g                                   |  134|
|Soy milk, unflavoured, 1 litre                        | 117|
|Soy sauce, 300ml                                       |134|
|Spaghetti - canned, 420g                               |142|
|Sports energy drinks, 250ml                            | 45|
|Sports energy drinks, 350ml                           |  45|
|Sugar - white, 1.5kg                                  | 142|
|Sultanas (supermarket only), 375g                     | 142|
|Sweets, 200g                                          | 134|
|Takeaway muffins and buns, each                       | 134|
|Tea bags (supermarket only), box of 100               | 142|
|Tea bags, flavoured or herbal, box of 25             |    6|
|Tea, takeaway                                         | 134|
|Tomato sauce - canned, 560g                          |   82|
|Tomatoes, 1kg                                        |  142|
|Tomatoes, canned, 400g                              |   134|
|Tuna - canned (supermarket only), 185g              |   142|
|Two minute noodles, multipack,5                      |  134|
|Vinegar, 750ml                                       |  134|
|Wheatmeal bread, sliced, 700g                         | 134|
|Wholegrain bread, sliced, 700g                        | 134|
|Yoghurt - flavoured, 150g pottle (supermarket o...    | 142|


#### Question 3
- When was 'Tuna - canned' cheapest?
##### Answer: Tuna was cheapest in April 2008.


#### Question 4 
- When was 'Tuna - canned' most expensive?
##### Answer: Tuna was most expensive in March 2018
 
#### Question 5
- Show the most cheapest product.
##### Answer: The most cheapest product is Baby food, 110g and cost 0,9 dollars in September 2007.

#### Question 6
- Show the most expensive product.

##### Answer: The most expensive product is Fresh Fish, 1 kg and cost 32,46 dollars in January 2018.


#### Question 7
- Show the top 10 cheapest food products


##### Answer: 
| Product					     | Amount   | Period |
|:--------------------------------------------------:|:--------:|:------:|
|Baby food, 110g  				     | 0.90  	|2007.09 |
|Bread - white sliced loaf, 600g		     | 1.01  	|2007.07 |
|Potatoes, 1kg					     | 1.05  	|2006.07 |
|Spaghetti - canned, 420g			     | 1.05  	|2008.03 |
|Tomatoes, canned, 400g				     | 1.05  	|2007.04 |
|Cabbage, 1kg	  				     | 1.06   	|2010.05 |
|Fruit flavoured drink powder, multipack of 3 to 5   | 1.09  	|2015.11 |
|Pineapple, pieces, in juice or syrup, canned, 425g  | 1.18 	|2008.04 |
|Chocolate novelty bars, 50g			     | 1.19  	|2007.05 |
|Cookie, takeaway, each				     | 1.29  	|2007.05 |



#### Question 8
- Show the top 10 most expensive food products.

##### Answer:
| Product					     | Amount   | Period |
|:--------------------------------------------------:|:--------:|:------:|
| Fresh fish, 1kg  				     | 32.46  	|2017.10 |
| Beef steak - porterhouse/sirloin, 1kg		     | 31.28  	|2017.05 |
| Avocado, 1kg	  				     | 23.05  	|2016.06 |
| Capsicums, green, else red, 1kg		     | 22.28  	|2012.08 |
| Infant formula, 900g 				     | 21.36  	|2015.04 |
| Beans, 1kg	  				     | 20.61  	|2016.07 |
| Prawns, frozen, 700g 				     | 20.53  	|2015.06 |
| Roasting lamb and hogget, fresh, chilled or frozen, 1kg| 18.79|2011.08 |
| Beef steak - blade, 1kg			     | 18.72  	|2018.01 |
| Courgettes, 1kg  				     | 18.43  	|2013.09 |


#### Question 9
- What was the average price for 1 kg bananas in 2012?

##### Answer: In 2012 was the average price for 1 kg bananas 2,598 dollars.

#### Question 10
- What was the average price for 1 kg bananas in 2013?

##### Answer: In 2013 was the average price for 1 kg bananas 2,645 dollars.


#### Question 11
- What was the price for 1 kg carrots in marts 2012?
##### Answer: In March 2012 the price for 1 kg carrots was 1,88 dollars.

#### Question 12
- What was the price for 1 kg carrots in marts 2013?
##### Answer: In March 2013 the price for 1 kg carrots was 2,14 dollars.

#### Question 13
- Show prices for kiwi in 2013.


#### Question 14
- In which period was 1 kg kiwi most expensive and what was the price? (Show top 10)


#### Question 15
- Show prices for apples in 2013


#### Question 16
- Show prices for bananas in 2013


#### Question 17
- Show prices for lettuce in 2013


#### Question 18
- Show the product prices in 2013


#### Question 19
- Show prices at canned food in 2017


#### Question 20
- Show how many times each product have been tested (ref question 2)