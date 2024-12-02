import json
import paho.mqtt.client as mqtt
from rules_engine import calculate_winter_supplement

# MQTT settings
BROKER = "test.mosquitto.org"
PORT = 1883

# Topic placeholders (replace with dynamic ID as needed)
INPUT_TOPIC = "BRE/calculateWinterSupplementInput/<MQTT topic ID>"
OUTPUT_TOPIC = "BRE/calculateWinterSupplementOutput/<MQTT topic ID>"

def on_message(client, userdata, message):
    """
    Callback when a message is received on the subscribed topic.
    """
    try:
        # Parse input JSON
        input_data = json.loads(message.payload.decode("utf-8"))
        
        # Process data through the rules engine
        result = calculate_winter_supplement(input_data)
        
        # Publish the result to the output topic
        client.publish(OUTPUT_TOPIC, json.dumps(result))
        print(f"Published: {result}")
    except Exception as e:
        print(f"Error processing message: {e}")

def main():
    """
    Main function to set up MQTT client and subscribe to the input topic.
    """
    client = mqtt.Client()
    client.on_message = on_message

    # Connect to MQTT broker
    print("Connecting to broker...")
    client.connect(BROKER, PORT, 60)

    # Subscribe to input topic
    client.subscribe(INPUT_TOPIC)
    print(f"Subscribed to: {INPUT_TOPIC}")

    # Start the loop
    client.loop_forever()

if __name__ == "__main__":
    main()
