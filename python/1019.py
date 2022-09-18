seconds = int(input())

hours = int(seconds / 3600)
remainingSeconds = seconds - hours * 3600;
minutes = int(remainingSeconds / 60)
remainingSeconds = remainingSeconds - minutes * 60;

print(f'{hours}:{minutes}:{remainingSeconds}')