local n = io.read('n')

local hours = n // 3600
n = n - hours * 3600
local minutes = n // 60
n = n - minutes * 60

print(string.format("%d:%d:%d", hours, minutes, n))