# 5-5-Property-Tax
 Calculates the assessment value and property tax for a piece of property using a function

## Scope
 A county collects property taxes on the assessment value of property, which is 60 percent of the property's actual value. For example, if an acre of land is valued at $10,000, its assessment value is $6,000. the property tax is then $0.72 for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the actual value of a piece of property and displays the assessment value and property tax.

 *Hint*: Ask the user for the actual value, and do all of the calculations in the main function. Then, send the two results to a showPropertyTax function to print.

## Sample Run
    Enter the actual value:  150000

    Assessed value: $90,000.00
    Property tax: $648.00

## Pseudocode
### Main function
    START
      SET ASSESSMENT_RATE = 0.6
      SET TAX_RATE = 0.72
      INPUT property_value
      CALCULATE assessment_value = property_value * ASSESSMENT_RATE
      CALCULATE property_tax = (assessment_value/100) * TAX_RATE
      CALL show_property_tax function
    END
### show_property_tax function
    START
      Pass In: assessment_value, property_tax
      PRINT assessment_value
      PRINT property_tax
    END
