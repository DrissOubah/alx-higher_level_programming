0. cURL body size
Write a Bash script that takes a URL, sends a request using curl, and displays the size of the body in bytes.
Example: ./0-body_size.sh 0.0.0.0:5000
1. cURL to the end
Write a Bash script that takes a URL, sends a GET request using curl, and displays the body of the response for a 200 status code.
Example: ./1-body.sh 0.0.0.0:5000/route_1
2. cURL Method
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response using curl.
Example: ./2-delete.sh 0.0.0.0:5000/route_3
3. cURL only methods
Write a Bash script that takes a URL and displays all HTTP methods the server will accept using curl.
Example: ./3-methods.sh 0.0.0.0:5000/route_4
4. cURL headers
Write a Bash script that takes a URL, sends a GET request using curl, and displays the body of the response. It must include the header X-School-User-Id: 98.
Example: ./4-header.sh 0.0.0.0:5000/route_5
5. cURL POST parameters
Write a Bash script that takes a URL, sends a POST request using curl with specific parameters, and displays the body of the response.
Example: ./5-post_params.sh 0.0.0.0:5000/route_6
Python Function:
6. Find a peak
Write a Python function find_peak that finds a peak in a list of unsorted integers.
Prototype: def find_peak(list_of_integers)
Constraints: No imports allowed, lowest complexity algorithm.
6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2).
Example: ./6-main.py tests the function with various inputs.
