# data_exploration

## Install dependencies 
Install dependencies gestionnary:<br/>
`pip install poetry` <br/>
Install dependencies:<br/>
`poetry install`

## Api functions
### Goal: get dataset you want from multiple source of data (opendatasoft v1/v2, Open Street Map, OFGl/datagouv)

Here are the links where you can see datasets availables:

OFGL: https://data.ofgl.fr/explore/?exclude.theme=INTERNE&sort=title <br/>
Opendatasoft V2: https://data.opendatasoft.com/explore/?disjunctive.language&disjunctive.source_domain_title&disjunctive.theme&disjunctive.semantic.classes&disjunctive.semantic.properties&sort=explore.popularity_score <br/>
Opendatasoft V1: https://public.opendatasoft.com/explore/?flg=fr&sort=modified <br/>
OSM: multiple sources/python packages <br/>

For all these sources the name of the dataset is define in the api tab when you select the dataset, this name id has to be passed in functions.

Related confluence page: https://ideamiage.atlassian.net/wiki/spaces/IDEA/pages/426315/Data+available
