export async function httpGet(url, callback) {
    try {
        let response = await fetch(url);
        const jsonResponse = await response.json();

        callback(jsonResponse);
    }
    catch (err) {
        console.log(`Request error: ${err}`);
        callback('');
    }
}