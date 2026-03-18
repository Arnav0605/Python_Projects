import os
import signal
from dotenv import load_dotenv
import elevenlabs

# Load environment variables from .env file if present
load_dotenv()

from elevenlabs import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

# Read API key and Agent ID from environment variables
API_KEY = "sk_888af7e9a9885594ff2152620bd715847bf13a6184e7e7a4"
AGENT_ID = "agent_0201kfwk74vbe9k90cc2vk3xjx2w"

# Initialize client with API key
client = ElevenLabs(api_key=API_KEY)

conversation = Conversation(
    # API client and agent ID.
    client,
    AGENT_ID,
    user_id="default_user",  # optional field - pass to constructor, not start_session()

    # Assume auth is required when API_KEY is set.
    requires_auth=bool(API_KEY),

    # Use the default audio interface.
    audio_interface=DefaultAudioInterface(),

    # Simple callbacks that print the conversation to the console.
    callback_agent_response=lambda response: print(f"Agent: {response}"),
    callback_agent_response_correction=lambda original, corrected: print(f"Agent: {original} -> {corrected}"),
    callback_user_transcript=lambda transcript: print(f"User: {transcript}"),

    # Uncomment if you want to see latency measurements.
    # callback_latency_measurement=lambda latency: print(f"Latency: {latency}ms"),

    # Uncomment if you want to receive audio alignment data with character-level timing.
    # callback_audio_alignment=lambda alignment: print(f"Alignment: {alignment.chars}"),
)

conversation.start_session()

signal.signal(signal.SIGINT, lambda sig, frame: conversation.end_session())

conversation_id = conversation.wait_for_session_end()
print(f"Conversation ID: {conversation_id}")
