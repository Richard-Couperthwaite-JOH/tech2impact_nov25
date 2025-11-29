# tech2impact_nov25
Additional helper code for the Tech2Impact Hackathon

1. write-file.yaml: a template to guide the creation of tools in ARK. We can use `ark create tool {name} -f {tool-specification-yaml}` to create the tool
   - This file also includes the template for the input json schema to use when creating a tool in the ARK UI
2. file_io.py: a simple code using Flask to read from text files and write to text files. these functions can be used in tools in ARK to increase functionality.
   - when running Flask, run it on `host="0.0.0.0"` to make sure that ARK can access the API
   - use `http://host.docker.internal:{port}` as the base API address in ARK
