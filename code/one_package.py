'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
import packaging

st.title("Package Data Analyzer")

# Get the packaging details from the user
package_details = st.text_input("Enter Package Information: ")

if package_details:
    # Parse the input string into structured package data
    package_structure = packaging.parse_packaging(package_details)
    overall_units = packaging.calc_total_units(package_structure)
    primary_unit = packaging.get_unit(package_structure)

    st.write("**Parsed Package Structure:**")
    # Display each level of the package information
    for level in package_structure:
        key = list(level.keys())[0]
        value = list(level.values())[0]
        st.info(f"{key} ➡ {value}")

    st.success(f"Total Package Size: {overall_units} {primary_unit}")