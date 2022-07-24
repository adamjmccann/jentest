from pymed import PubMed

# Create a PubMed object that GraphQL can use to query
# Note that the parameters are not required but kindly requested by PubMed Central
# https://www.ncbi.nlm.nih.gov/pmc/tools/developers/
pubmed = PubMed(tool="JenTest", email="mccann232@gmail.com")


## REPLACE WITH JENNY CSV READ IN CODE
proteins = {
    "desmin",
    "Tubulin"
}


# Create a GraphQL query in plain text
for protein in proteins:
    print("Searching for " + protein)
    queryIn = "{0}[Title]".format(protein)
    # print (" -- " + query)
    
    # results = pubmed.query(queryIn)
    resultsCount = pubmed.getTotalResultsCount(queryIn)    
    print(" --  found {0} results".format(resultsCount))

    # articleList = []
    # articleInfo = []
    # for article in results:
    #     articleDict = article.toDict()
    #     articleList.append(articleDict)
        

# query = "occupational health[Title]"


# # Execute the query against the API
# results = pubmed.query(query, max_results=500)

# # Loop over the retrieved articles
# for article in results:

#     # Print the type of object we've found (can be either PubMedBookArticle or PubMedArticle)
#     print(type(article))

#     # Print a JSON representation of the object
#     print(article.toJSON())

