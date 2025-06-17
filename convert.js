document.getElementById('get-start-btn').addEventListener('click', () => {
  document.querySelector('.splash-screen').style.display = 'none';
  document.querySelector('.exchange-screen').style.display = 'block';
});
document.getElementById('convert').addEventListener('click', async () => {
    const amount = document.getElementById('amount').value;
    const fromCurrency = document.getElementById('fromCurrency').value;
    const toCurrency = document.getElementById('toCurrency').value;
  
    if (amount === '' || isNaN(amount)) {
      alert('Please enter a valid amount');
      return;
    }
  
    const response = await fetch(`https://api.exchangerate-api.com/v4/latest/${fromCurrency}`);
    const data = await response.json();
  
    const rate = data.rates[toCurrency];
    const convertedAmount = (amount * rate).toFixed(2);
  
    document.getElementById('result').textContent = 
      `${amount} ${fromCurrency} = ${convertedAmount} ${toCurrency}`;
  });
  
  document.getElementById('swap').addEventListener('click', () => {
    const fromCurrency = document.getElementById('fromCurrency');
    const toCurrency = document.getElementById('toCurrency');
    const temp = fromCurrency.value;
    fromCurrency.value = toCurrency.value;
    toCurrency.value = temp;
  });

  

  