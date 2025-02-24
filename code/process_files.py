'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import streamlit as st
import packaging
import json
from io import StringIO

st.title("Batch Package File Processor")

if "file_summaries" not in st.session_state:
    st.session_state.file_summaries = []
if "files_count" not in st.session_state:
    st.session_state.files_count = 0
if "packages_count" not in st.session_state:
    st.session_state.packages_count = 0

uploaded = st.file_uploader("Upload your package text file:")

if uploaded:
    original_name = uploaded.name
    output_name = original_name.replace(".txt", ".json")
    all_packages = []
    content = StringIO(uploaded.getvalue().decode("utf-8")).read()

    for line in content.splitlines():
        clean_line = line.strip()
        if clean_line:
            pkg = packaging.parse_packaging(clean_line)
            all_packages.append(pkg)

    num_packages = len(all_packages)
    with open(f"./data/{output_name}", "w") as out_file:
        json.dump(all_packages, out_file, indent=4)

    summary_text = f"{num_packages} packages written to {output_name}"
    st.session_state.file_summaries.append(summary_text)
    st.session_state.files_count += 1
    st.session_state.packages_count += num_packages

    for summary in st.session_state.file_summaries:
        st.info(summary, icon="💾")
    
    st.success(
        f"{st.session_state.files_count} files processed, {st.session_state.packages_count} total packages processed"
    )