import subprocess

# Variables for the user
browser = 'librewolf.exe'
speech_instance = "lbry2.vanwanet.com/speech"

link = input("Link: ")
link = link.replace('#', ':')
link = link.replace('lbry.ix.tc', speech_instance)
link = link.replace('librarian.davidovski.xyz', speech_instance)
link = link.replace('madiator.com', speech_instance)
link = link.replace('odysee.com', speech_instance)
link = link.replace('lbry:/', 'https://spee.ch')
link = link.replace('librarian.davidovski.xyz', speech_instance)

subprocess.Popen([browser, link])
