# Dev Log
## June 9th and prior
I've completed a couple of scripts to explore the data; trying to get a better idea of the composition and subject matter. Abstraction has been emphasized so the framework can remain flexible as the direction of the project emerges.

### Changes
- Created [dbConstruct](dbConstruct.py)
  - dbConstruct is a library for dynamic .h5 database generation. By passing a .json of fields in the format [{"type":"<int,string>", "id":"<column id>"},{"type":"<int,string>", "id":"<column id>"},...], a codebase compatible .h5 database is created.
  - These databases are designed to be universally accessible by the rest of the code, making it easier for us to consolidate data as we move forward. Ideally we will be able to reference as many different sources as possible simultaneously, to get the biggest picture possible.
  - Beyond code comments, documentation is being written alongside the code to clearly outline
  both the process and maximize usability into the future.
- Created [req_bos](req_bos.py)
  - req_bos is a library to cleanly make requests to the [Analyze Boston](https://data.boston.gov/) site. It plugs directly into the dbConstruct and facilitates download of the data as well as the abstraction of the resources.
- Created [eda](eda.py)
  - eda is the exploratory data analysis. Not much to be said as it has produced minimal results so far other than confirming that the rest of the code works.