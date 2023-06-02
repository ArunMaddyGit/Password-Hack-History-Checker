import requests
import hashlib

def getApiData(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Problem with API: {res.status_code},')
  return res

def passwordLeakCount(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def passCheck(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = getApiData(first5_char)
  return passwordLeakCount(response, tail)

def main(password):
  count = passCheck(password)
  if count:
    msg=f'Your Password has been breached {count} times'
  else:
    msg=f'Your Password has never been breached before.'
     
  return msg


