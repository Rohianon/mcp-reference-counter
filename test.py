import itertools

import httpx
from scholarly import scholarly

def get_citeas_data(resource: str) -> str:
    """
    Retrieve BibteX-formatted citation for the specified `resource` (e.g., DOI, URL, Keyword) from the CiteAs
    """
    response = httpx.get(f"https://api.citeas.org/product/{resource}?email=default@example.com")
    response.raise_for_status()
    data = response.json()
    return next((export['export'] for export in data['exports'] if export['export_name'] == 'bibtext'), None)

def get_scholar_data(query: str, results: int = 2) -> str:
    """
    Retrieves `results` BitTex-formatted citations for publications matching the `query` from the Google Scholar.
    """
    pubs = scholarly.search_pubs(query)
    return "\n".join(scholarly.bibtext(pub) for pub in itertools.islice(pubs, results))
                

if __name__ == "__main__":
    # test the two functions above
    citeas_bibtex = get_citeas_data("Monetory policies")
    print("CiteAs BibTeX:\n", citeas_bibtex)

    scholar_bibtex = get_scholar_data("quantum entanglement", results=2)
    print("Google Scholar BibTeX:\n", scholar_bibtex)
    
