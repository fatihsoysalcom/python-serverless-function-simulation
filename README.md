# Python Serverless Function Simulation

This example demonstrates the core concept of a serverless function (Function-as-a-Service) using a simple Python HTTP server. It simulates small, independent code units that are triggered by HTTP requests, process input, and return a response, without requiring explicit server management from the developer's perspective. The functions are stateless and designed for specific tasks, mirroring how serverless platforms like AWS Lambda or Azure Functions operate.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run the script from your terminal: `python main.py`
3. Test the simulated functions using `curl`:
   - `curl http://localhost:8000/hello?name=DevToUser`
   - `curl http://localhost:8000/info`
   - `curl -X POST -H "Content-Type: application/json" -d '{"input": "sample data"}' http://localhost:8000/process_data`

## Original Article

This example accompanies the Turkish article: [Open Serverless v4 ile Sunucusuz Geleceğe Adım Atın: Yenilikler ve Uygulama Rehberi](https://fatihsoysal.com/blog/open-serverless-v4-ile-sunucusuz-gelecege-adim-atin-yenilikler-ve-uygulama-rehberi/).

## License

MIT — see [LICENSE](LICENSE).
