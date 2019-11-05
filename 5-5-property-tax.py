# 5-5 Property Tax
# Shaun Hayworth
# CIS 2
# 11-04-2019
# Source code and revision history are available at https://github.com/SCHayworth/5-5-Property-Tax

# Program gets a property value from the user, then calculates an assessment value of 60% of the original property value, and the tax
# for the property equal to $0.72 per $100 of the assessment value.

# Define the main() function
# Mainline program logic
def main():

    # Initialize constants for the assessment rate and tax rate.
    # Change these values to make calculations with different assessment and tax rates.
    ASSESSMENT_RATE = 0.6 # Assessment value is 60% of the total property value
    TAX_RATE = 0.72 # Property tax is $0.72 for every $100 of the assessment value

    # Prompt user for the property value.
    property_value = float(input('Enter the actual value: '))

    # Calculate the assessment value
    assessment_value = property_value * ASSESSMENT_RATE

    # Calculate tax based on each $100 of the assessment value
    property_tax = (assessment_value / 100) * TAX_RATE

    # Call the show_property_tax() function
    show_property_tax(assessment_value, property_tax) # Displays the assessed value and property tax

# Define the show_property_tax(value, tax) function.
# Accepts arguments for the assessment value and the property tax, and prints them to the screen
def show_property_tax(value, tax):

    # Print the assessment value and the property tax to the screen
    print(f'\nAssessed value: ${value:,.2f}')
    print(f'Property tax: ${tax:,.2f}')

# Call the main() function to execute the program
main()
