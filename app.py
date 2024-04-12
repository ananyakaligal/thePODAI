import random

import azure.cognitiveservices.speech as speechsdk

import script

# import script

# Creates an instance of a speech config with specified subscription key and service region.
speech_key = ""
service_region = "eastus"

# Different voices
voices = ['en-US-AndrewNeural', 'en-US-AvaNeural', 'en-US-AriaNeural', 'en-US-BrianNeural', 'en-US-JaneNeural', 'en-US-JennyNeural', '']

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
# Note: the voice setting will not overwrite the voice element in input SSML.

# Note : you can use random.choice(voices) to take any random voice also,
# You can use any one for specifying
speech_config.speech_synthesis_voice_name = 'en-US-AriaNeural'

text = script.script

# use the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

audio_config = speechsdk.audio.AudioOutputConfig(filename="./output.mp3")
result = speech_synthesizer.speak_text_async(text).get()


# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Done!")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))

print(voices)