#
# hw3pr4.py - extra credit problem "Sounds Good!"
#
# Name: Brian Richardson
#
#
import imp
import csaudio ; imp.reload(csaudio) ; from csaudio import *
import math
# The example changeSpeed function
def changeSpeed(fileName, newSampleRate, newFile = "out.wav"): 
    """ changeSpeed takes in 
           fileName, a string indicating the sound you wish to use. 
           newSampleRate, an integer representing the new sample rate you want, 
                  in units of samples per second. 
           newFile, an OPTIONAL string indicating the name to which 
                  you wish to save the speed-changed sound. 
                  If you don't specify a second input to changeSpeed, 
                  the new sound will be saved as "out.wav" 
          changeSpeed creates a new file (using the name in newFile) 
             that uses the same sound data, but runs it at the 
             samplerate of newSampleRate samples per second. 
             It plays the new sound and then does not return anything... 
       """ 
       # This next function call returns TWO values: 
       # samples is a LIST of the raw sound data 
       # oldSampleRate is the old sample rate, in samples per second 
       # 
       # This will be the standard way to get sound data from a file. samples, oldSampleRate = readWav(fileName) 
    samples, oldSampleRate = readWav(fileName)
       # This next function call does not return any value, but 
       # it does write the sound data in the list "samples" into 
       # a file whose name is the string in the newFile variable 
       # It uses the new sample rate instead of the old. writeWav(samples, newSampleRate, newFile)
    writeWav(samples,newSampleRate,newFile)
       # This next call to play also does not return a value, 
       # but it plays the sound in the file named newFile. play(newFile)
    play(newFile)
       # Now, we return the list of the sound data - it won't always 
       # be needed, we return it just in case it is. 
       # actually, let's comment this out for now... 
    return samples

# The example flipflop function
def flipflop(fileName, newFile = "out.wav"): 
     """ flipflop takes in fileName, a string indicating the sound you wish to use.     
         newFile, an OPTIONAL string indicating the name to which 
                  you wish to save the flip-flopped sound. 
                  If you don't specify a second input to flipflop, 
                  the new sound will be saved as "out.wav" 
         
         flipflop creates a new file (using the name in newFile) 
             that uses the same sound data, but with the first and second 
             halves of the sound interchanged. 

        flipflop plays the new sound that it creates (no return value) 
      """
     samples, sampleRate = readWav(fileName)
     length = len(samples)
     newSamples = samples[length // 2:] + samples[:length // 2] # flip flop
     writeWav(newSamples, sampleRate, newFile)
     play(newFile) # play the new sound for good measure
     return newSamples # return the new sound data list - commented for now

def reverse(fileName, newFile = "out.wav"):
    samples, sampleRate = readWav(fileName)
    length = len(samples)
    newSamples = samples[::-1]
    writeWav(newSamples,sampleRate,newFile)
    play(newFile)
    return newSamples

def volume(fileName, fraction, newFile = "out.wav"):
    samples, sampleRate = readWav(fileName)
    length = len(samples)
    newSamples = [i * fraction for i in samples]
    writeWav(newSamples,sampleRate,newFile)
    play(newFile)
    return newSamples

def oneFreq(freq, newFile = "out.wav"):
    sampleRate = 22050
    samples = [32767.0*math.sin((2*math.pi*x)/(sampleRate/freq)) for x in range(sampleRate)]
    writeWav(samples,sampleRate,newFile)
    play(newFile)
    return samples

def oneFreq(freq, power = 1.0, audible=True,newFile = "out.wav"):
    '''Added parameter audible
    if audible == True plays and outputs wav file, otherwise just returns the samples
    '''
    sampleRate = 22050
    amp = power * 32767.0
    samples = [amp*math.sin((2*math.pi*x)/(sampleRate/freq)) for x in range(sampleRate)]
    if audible:
        writeWav(samples,sampleRate,newFile)
        play(newFile)
    return samples
def multiFreq(sounds, newFile = "out.wav"):
    '''
    Works with any number of given sounds as long as they are in the correct format
    Format: [[freq0,power0],[freq1,power1],[freq2,power2],[freq3,power3],~~~~~~~~]
    '''
    sampleRate = 22050
    rawSamples = []
    print("Total # of sounds:", len(sounds))
    for soundIndex in range(len(sounds)):
        print("Sound Index:",soundIndex)
        rawSamples.append((oneFreq(sounds[soundIndex][0],sounds[soundIndex][1])))
    avgSamples = []
    for i in range(sampleRate):
        sampleSum = 0.0
        for sampleIndex in range(len(rawSamples)):
            sampleSum = sampleSum + rawSamples[sampleIndex][i]
        avgSample = sampleSum/len(rawSamples)
        avgSamples.append(avgSample)
    writeWav(avgSamples,sampleRate,newFile)
    play(newFile)
    return avgSamples
    
def climbSteps(freq, steps, newFile = "out.wav"):
    '''
    Question #5 Custom Function
    climbSteps takes a given frequency and climbs by a given number of half steps
    This function only plays the final half-step climbing sound
    '''
    sampleRate = 22050
    hStep = 1.05946309436
    wStep = 1.122462048309373
    samples = []
    for i in range(steps+1):
        samples = samples + oneFreq(freq*hStep**i,1.0,False)
    writeWav(samples,sampleRate,newFile)
    play(newFile)
    return samples
        
    
