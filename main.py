from pyscript import document, display

def order(e):

# Prices
  burger = 5
  fries = 3
  soda = 1

# Detecting the checkboxes
  burger_ordered = float(document.getElementById("burger").checked)
  fries_ordered = float(document.getElementById("fries").checked)
  soda_ordered = float(document.getElementById("soda").checked)

# Calculating (w/ Booleans returning 1s and 0s)
  subtotal = float(burger * burger_ordered + fries * fries_ordered + soda * soda_ordered)

# 12% vat
  vat = subtotal * 0.12

# After vat
  total = subtotal + vat

#  Displaying the receipt
  document.getElementById("subtotal").innerText = f"${subtotal}"
  document.getElementById("vat").innerText = f"${vat}"
  document.getElementById("total").innerText = f"${total}"
