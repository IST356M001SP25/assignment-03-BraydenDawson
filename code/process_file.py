'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st
import packaging
import json
from io import StringIO

st.title("Package File Processor")

uploaded_file = st.file_uploader("Select a package data file:")

if uploaded_file:
    original_name = uploaded_file.name
    output_name = original_name.replace(".txt", ".json")
    processed_packages = []
    file_content = StringIO(uploaded_file.getvalue().decode("utf-8")).read()

    for record in file_content.splitlines():
        record = record.strip()
        if record:  
            parsed_data = packaging.parse_packaging(record)
            total_units = packaging.calc_total_units(parsed_data)
            base_unit = packaging.get_unit(parsed_data)
            processed_packages.append(parsed_data)
            st.info(f"{record} ➡ Total Size: {total_units} {base_unit}")

    package_count = len(processed_packages)
    with open(f"./data/{output_name}", "w") as output_file:
        json.dump(processed_packages, output_file, indent=4)
        
    st.success(f"{package_count} packages have been saved to {output_name}", icon="💾")
    ###
    ###