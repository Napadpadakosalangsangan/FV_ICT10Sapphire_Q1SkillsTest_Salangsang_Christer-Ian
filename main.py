from pyscript import document, display

def order(e):

  burger_ordered = float(document.getElementById("burger").value)
  fries_ordered = float(document.getElementById("fries").value)
  soda_ordered = float(document.getElementById("soda").value)

  subtotal = float(burger_ordered + fries_ordered + soda_ordered)

  vat = subtotal * 0.12

  total = subtotal + vat

  document.getElementById("subtotal").innerText = f"${subtotal}"
  document.getElementById("vat").innerText = f"${vat}"
  document.getElementById("total").innerText = f"${total}"
