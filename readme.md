
Here’s a detailed README.md file for this test mqtt project:

Winter Supplement Rules Engine
This project implements a business rules engine that determines eligibility and calculates the Winter Supplement benefits based on predefined criteria. The solution uses an event-driven architecture and integrates with an MQTT broker for communication.

Project Structure
graphql
Copy code
Test Software/
│
├── src/
│   ├── rules_engine.py          # The rules engine implementation
│   ├── mqtt_client.py           # MQTT client for communication
│
├── tests/
│   ├── test_rules_engine.py     # Unit tests for the rules engine
│
├── venv/                        # Virtual environment folder
│
├── .gitignore                   # Git ignore file
├── README.md                    # Documentation
└── pytest.ini                   # Pytest configuration (optional)
Prerequisites
Python 3.8+
pip for installing dependencies
An MQTT broker (e.g., test.mosquitto.org on port 1883)



Setup Instructions

1. Clone the Repository
bash
Copy code
git clone https://github.com/Kingcollins004/MQTT-test.git
cd Test Software

2. Create a Virtual Environment
bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Update the MQTT Topic ID
To integrate the rules engine with the Winter Supplement web app, you need to update the MQTT Topic ID. This ID can be retrieved from the Winter Supplement Calculator.

Update the topic ID in the mqtt_client.py file:

python
Copy code
BRE/calculateWinterSupplementInput/<MQTT topic ID>
BRE/calculateWinterSupplementOutput/<MQTT topic ID>
Replace <MQTT topic ID> with the unique ID obtained from the web app.

How to Run the Rules Engine
Start the rules engine by running the mqtt_client.py script:

bash
Copy code
python src/mqtt_client.py
Ensure that the Winter Supplement Calculator is sending input data to the specified MQTT topic.

How to Run Unit Tests
Ensure you’re in the root directory.
Run the following command:
bash
Copy code
pytest
This will discover and execute all the test cases in the tests/ folder. For detailed output, run:

bash
Copy code
pytest -v
Features
Eligibility Determination: Checks if a family unit is eligible for the Winter Supplement.
Supplement Calculation:
Base Amount: Based on family composition (single, couple, family with children).
Children Amount: Additional supplement for dependent children.
Event-Driven Architecture: Communicates with the Winter Supplement Calculator via MQTT.
Input and Output Data Format
Input Format
The rules engine expects the following JSON format:

json
Copy code
{
  "id": "str",  // Unique ID for the input
  "numberOfChildren": "int",  // Number of dependent children
  "familyComposition": "str", // Options: ["single", "couple"]
  "familyUnitInPayForDecember": "bool" // Determines eligibility
}
Output Format
The output JSON will look like:

json
Copy code
{
  "id": "str",               // Input ID
  "isEligible": "bool",      // Eligibility status
  "baseAmount": "float",     // Base supplement amount
  "childrenAmount": "float", // Supplement amount for children
  "supplementAmount": "float" // Total supplement amount
}
Unit Test Details
The project includes unit tests for the rules engine in tests/test_rules_engine.py. These test cases cover:

Clients not eligible for December payment.
Single clients without children.
Families with dependent children.
MQTT Broker Details
The MQTT broker facilitates communication between the Winter Supplement web app and the rules engine. The project uses:

Host: test.mosquitto.org
Port: 1883
Ensure the broker is available and configured correctly.

Author
[Your Name]
For any questions, feel free to contact ISD.ApplicationModernizationProgram@gov.bc.ca.