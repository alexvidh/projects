from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev')
openButton = driver.find_element_by_xpath('//*[@id="add_new_todo"]/img')
openButton.click()

selectCategory = driver.find_element_by_id('select2-select_category-container')
selectCategory.click()

selectNewCategory = driver.find_element_by_xpath('/html[1]/body[1]/span[1]/span[1]/span[2]/ul[1]/li[last()]')
selectNewCategory.click()

inputProjectTitle = driver.find_element_by_xpath('//*[@id="project_title"]')
inputProjectTitle.click()
inputProjectTitle.send_keys('Change the parameter matcher used in parsing step text. The change is immediate and may be performed between step definitions in your step implementation modules - allowing adjacent steps to use different matchers if necessary. There are several parsers available in behave (by default):parse (the default, based on: parse)Provides a simple parser that replaces regular expressions for step parameters with a readable syntax like. The syntax is inspired by the Python builtin string.format() function. Step parameters must use the named fields syntax of parse in step definitions. The named fields are extracted, optionally type converted and then used as step function arguments.')

inputProjectText = driver.find_element_by_xpath('//*[@id="project_text"]')
inputProjectText.click()
inputProjectText.send_keys('Change the parameter matcher used in parsing step text. The change is immediate and may be performed between step definitions in your step implementation modules - allowing adjacent steps to use different matchers if necessary. There are several parsers available in behave (by default):parse (the default, based on: parse)Provides a simple parser that replaces regular expressions for step parameters with a readable syntax like. The syntax is inspired by the Python builtin string.format() function. Step parameters must use the named fields syntax of parse in step definitions. The named fields are extracted, optionally type converted and then used as step function arguments.')

driver.save_screenshot('max_text_results.png')