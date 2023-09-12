# importing libraries
import time
import speech_recognition as sr
import os
import pyperclip
#/Users/maliq/Downloads/test.wav
import pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence

r = sr.Recognizer()
cwd = os.getcwd()

def get_large_audio_transcription(path):
    print('\033[1;37m')
    print('\n' * 50)

    Namecorrections = []
    Nameerrors = []
    Gencorrections = []
    Generrors = []

    NamesFile = open(f'{cwd}/Name')
    Namelines = NamesFile.readlines()

    for line in Namelines:
        try:
            NameError = line.split(':', 1)[0]
            NameError = NameError
            Nameerrors.append(NameError)

            NameCorrection = line.split(':', 1)
            if len(NameCorrection) > 0:
                NameCorrection = NameCorrection[1]
            Namecorrections.append(NameCorrection)
            print(f'Name Error Added: {NameError}')
            print(f'Name Correction Added: {NameCorrection}')
        except:
            pass

    GenFile = open(f'{cwd}/Gen')
    Genlines = GenFile.readlines()

    for linew in Genlines:
        try:
            GenError = linew.split(':', 1)[0]
            GenError = GenError
            Generrors.append(GenError)

            GenCorrection = linew.split(':', 1)
            if len(GenCorrection) > 0:
                GenCorrection = GenCorrection[1]
            Gencorrections.append(GenCorrection)

            print(f'General Error Added: {GenError}')
            print(f'General Correction Added: {GenCorrection}')
        except:
            pass

    time.sleep(2)
    # a function that splits the audio file into chunks
    # and applies speech recognition

    print('\n' * 50)
    input('Enter To Start Program: ')

    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=500,
                              # adjust this per requirement
                              silence_thresh=sound.dBFS - 14,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=500,
                              )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                from io import StringIO
                import sys
                tmp = sys.stdout
                my_result = StringIO()
                sys.stdout = my_result

                text = r.recognize_google(audio_listened)

                sys.stdout = tmp
                response = my_result.getvalue()

                # Split the response by the first comma and extract the first part
                response = response.split(',', 1)[0]

                # Split the response by the first colon
                lis = response.split(':', 1)
                if len(lis) > 1:
                    lis = lis[1]
                else:
                    lis = None  # Handle the case where there's no colon in the response

                # Now you can safely split lis again (if it's not None)
                if lis is not None:
                    lis = lis.split(':', 1)
                    if len(lis) > 1:
                        confidence = lis[1]
                    else:
                        confidence = None  # Handle the case where there's no colon in lis

                    # Process confidence (if it's not None)
                    if confidence is not None:
                        confidence = confidence.split('.', 1)
                        if len(confidence) > 1:
                            confidence = confidence[1]
                        else:
                            confidence = None  # Handle the case where there's no dot in confidence

                        # Remove the last 6 characters (if confidence is not None)
                        if confidence is not None and len(confidence) >= 6:
                            confidence = confidence[:-6]

            except sr.UnknownValueError as e:
                print("Error:", str(e))

            else:
                text = f"{text.capitalize()}. "
                print('\n' * 50)
                print('Program Still Running')
                whole_text = f'{whole_text} {text}'
                rt = open(f'{cwd}/text', 'a')

                count = 0

                for error in Nameerrors:
                    count += 1
                    if error in text:
                        text = text.replace(error, Namecorrections[count - 1])
                        print(f'Corrected Name: {text}')
                    else:
                        pass


                countt = 0
                for error in Generrors:
                    countt += 1
                    if error in text:
                        print(error)
                        if int(confidence) <= 64:
                            text = text.replace(error, Gencorrections[countt - 1])
                            print(f'Corrected Text: {text}')
                        else:
                            print(f'confidence suggests purposeful statement: [{confidence}]')
                    else:
                        pass

                rt.write(f'\n{text}')

                rt.close()

    # return the text for all chunks detected
    print('Text Gathered')
    os.system('say Program Completed: all text gatherd')

def man():
    print('\n'*100)
    print('''
=================================
\033[0;31m     ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄ 
\033[0;34m    █   █    █ █ █   ▐ 
\033[0;31m    ▐  █    █     ▀▄   
\033[0;34m       █   ▄▀  ▀▄   █  
\033[0;31m        ▀▄▀     █▀▀▀   
\033[0;34m                ▐     
=================================
Developed By \033[1;32m JDX50S
=================================
\033[1;35m1 = copy previous to clipboard
\033[1;37m=================================
\033[1;36m2 = clear output file
\033[1;37m=================================
\033[1;34m3 = convert audio .m4a -> .wav  
\033[1;34m3 = then launch Voice Recognition
\033[1;37m=================================
\033[1;31m4 = launch Voice Recognition
\033[1;37m=================================
\033[1;32m5 = append known names errors
\033[1;37m=================================
\033[1;33m6 = append known common errors
\033[1;37m=================================''')

    fi = input('Enter a value: ')
    print('\033[1;37m')
    try:
        int(fi)
    except:
        print('system exit')
        exit(0)

    if int(fi) == 1:
        text = open(f'{cwd}/text', 'r')
        textlines = text.read()
        pyperclip.copy(textlines)
        print('\033[0;31mCopied To Clipboard')
        exit(0)

    if int(fi) == 2:
        text = open(f'{cwd}/text','w')
        print('\033[0;31mOutput cleared')
        time.sleep(2.5)
        man()

    elif int(fi) == 3:
        m4a_file = input('Enter .m4a File: ')
        wav = f"{m4a_file[:-4]}.wav"
        from pydub import AudioSegment

        track = AudioSegment.from_file(m4a_file, format='m4a')
        file_handle = track.export(wav, format='wav')

        print(f'\033[0;31m{m4a_file}->{wav}')
        path = wav
        get_large_audio_transcription(path)

    elif int(fi) == 4:
        path = input('Enter .wav File: ')
        get_large_audio_transcription(path)

    elif int(fi) == 5:
        names = open(f'{cwd}/Name','a')
        nameerror = input('Incorrect name interpretation: ')
        namecorrection = input('Correct name interpretation: ')
        update = f'\n{nameerror}:{namecorrection}'
        names.write(update)
        print('\033[0;31mPreference added @name')
        time.sleep(2.5)
        man()

    elif int(fi) == 6:
        general = open(f'{cwd}/Gen','a')
        generalerror = input('General error: ')
        correction = input('Correct replacement: ')
        update = f'\n{generalerror}:{correction}'
        general.write(update)
        print('\033[0;31mPreference added @general')
        time.sleep(2.5)
        man()

    else:
        print('system exit')
        exit(0)

man()


