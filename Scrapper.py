import requests
import json
import base64

def get_products(from_index, to_index):
    url = "https://www.corona.cl/_v/segment/graphql/v1"
   
    variables = {
        "hideUnavailableItems": True,
        "skusFilter": "ALL_AVAILABLE",
        "simulationBehavior": "default",
        "installmentCriteria": "MAX_WITHOUT_INTEREST",
        "productOriginVtex": False,
        "map": "c,c",
        "query": "moda/hombre",
        "orderBy": "OrderByReleaseDateDESC",
        "from": from_index,
        "to": to_index,
        "selectedFacets": [
            {"key": "c", "value": "moda"},
            {"key": "c", "value": "hombre"}
        ],
        "facetsBehavior": "Static",
        "categoryTreeBehavior": "default",
        "withFacets": False,
        "advertisementOptions": {
            "showSponsored": True,
            "sponsoredCount": 3,
            "advertisementPlacement": "top_search",
            "repeatSponsoredProducts": True
        }
    }
   
    encoded_variables = base64.b64encode(json.dumps(variables).encode()).decode()
   
    params = {
        "workspace": "master",
        "maxAge": "short",
        "appsEtag": "remove",
        "domain": "store",
        "locale": "es-CL",
        "__bindingId": "652112c1-5f0e-4923-b587-f06d7f1cc1b0",
        "operationName": "productSearchV3",
        "variables": "{}",
        "extensions": json.dumps({
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "3e2c473672fc986dc5377d35560f5d5244fbca3698414bd02772c649d67994b6",
                "sender": "vtex.store-resources@0.x",
                "provider": "vtex.search-graphql@0.x"
            },
            "variables": encoded_variables
        })
    }
   
    response = requests.get(url, params=params)
    return response.json()

def scrape_all_products():
    all_products = []
    from_index = 0
    to_index = 47
   
    while True:
        data = get_products(from_index, to_index)
        products = data['data']['productSearch']['products']
       
        if not products:
            break
       
        all_products.extend(products)
        print(f"Obtenidos {len(all_products)} productos hasta ahora...")
        from_index = to_index + 1
        to_index += 48
   
    return all_products

def clean_product_data(products):
    cleaned_products = []
    product_id = 1

    for product in products:
        cleaned_product = {
            'id': product_id,
            'title': product.get('productName', ''),
            'precio': None,
            'image': ''
        }
       
        price_range = product.get('priceRange', {})
        if isinstance(price_range, dict):
            selling_price = price_range.get('sellingPrice', {})
            if isinstance(selling_price, dict):
                cleaned_product['precio'] = selling_price.get('lowPrice')
       
        items = product.get('items', [])
        if items and isinstance(items[0], dict):
            images = items[0].get('images', [])
            if images and isinstance(images[0], dict):
                cleaned_product['image'] = images[0].get('imageUrl', '')
       
        cleaned_products.append(cleaned_product)
        product_id += 1

    return cleaned_products

def save_to_json(products, filename="productos_limpios.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    print(f"Productos guardados en {filename}")

def main():
    try:
        all_products = scrape_all_products()
        print(f"Total de productos obtenidos: {len(all_products)}")
       
        cleaned_products = clean_product_data(all_products)
       
        save_to_json(cleaned_products)
       
    except Exception as e:
        print(f"Ocurrió un error inesperado: {str(e)}")

if __name__ == "__main__":
    main()