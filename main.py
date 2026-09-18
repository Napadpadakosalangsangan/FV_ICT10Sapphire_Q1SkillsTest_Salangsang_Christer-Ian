from pyscript import document, display

def order(e):

  burger = 5
  fries = 3
  soda = 1

# How do I let my pyscript know if it's checked or not T-T
  burger_ordered = float(document.getElementById("burger").checked)
  fries_ordered = float(document.getElementById("fries").checked)
  soda_ordered = float(document.getElementById("soda").checked)

  subtotal = float(burger * burger_ordered + fries * fries_ordered + soda * soda_ordered)

  vat = subtotal * 0.12

  total = subtotal + vat

  document.getElementById("subtotal").innerText = f"${subtotal}"
  document.getElementById("vat").innerText = f"${vat}"
  document.getElementById("total").innerText = f"${total}"
