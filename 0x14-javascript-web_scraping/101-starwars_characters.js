#!/usr/bin/node

const request = require('request'); // Import the 'request' module for making HTTP requests
const id = process.argv[2]; // Get the movie ID from the command-line arguments
const url = `https://swapi-api.alx-tools.com/api/films/${id}`; // Construct the URL for the specified movie

request.get(url, (error, response, body) => {
	if (error) {
		console.log(error); // Log any errors that occur during the request
		} else {
			const content = JSON.parse(body); // Parse the response body as JSON
			const characters = content.characters; // Extract the list of character URLs from the movie data
			    
			// Loop through each character URL
			for (const character of characters) {
				// Make a GET request to each character URL
				request.get(character, (error, response, body) => {
					if (error) {
						console.log(error); // Log any errors that occur during the request
						} else {
							const names = JSON.parse(body); // Parse the response body as JSON
							console.log(names.name); // Print the name of the character
							}
					});
				}
			}
});
