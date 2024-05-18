const BASE_URL = 'http://localhost:8000/api/';

export async function getListObjectsFromServer(typeObjects, query, limit = 10, offset = 0) {
  let url = new URL(BASE_URL + typeObjects + '/');


  if (query) {
    Object.keys(query).forEach(key => url.searchParams.append(key, query[key]));
  }

  if (limit) {
    url.searchParams.append('limit', limit);
  }
  if (offset) {
    url.searchParams.append('offset', offset);
  }

  return fetch(url).then(response => response.json());
}