import React, { useState } from 'react';

function App() {
  const [formData, setFormData] = useState({
    age: '',
    anaemia: '',
    diabetes: '',
    high_blood_pressure: '',
    sex: '',
    smoking: ''
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...formData,
          age: parseFloat(formData.age),
          anaemia: parseInt(formData.anaemia),
          diabetes: parseInt(formData.diabetes),
          high_blood_pressure: parseInt(formData.high_blood_pressure),
          sex: parseInt(formData.sex),
          smoking: parseInt(formData.smoking),
        })
      });

      const data = await response.json();
      setResult(data.message || data.error);
    } catch (err) {
      setResult("Something went wrong.");
    }
  };

  return (
    <div className="App">
      <h2>Heart Failure Prediction</h2>
      <form onSubmit={handleSubmit}>
        <input type="number" name="age" placeholder="Age" onChange={handleChange} required />
        <input type="number" name="anaemia" placeholder="Anaemia (0/1)" onChange={handleChange} required />
        <input type="number" name="diabetes" placeholder="Diabetes (0/1)" onChange={handleChange} required />
        <input type="number" name="high_blood_pressure" placeholder="High BP (0/1)" onChange={handleChange} required />
        <input type="number" name="sex" placeholder="Sex (0=F, 1=M)" onChange={handleChange} required />
        <input type="number" name="smoking" placeholder="Smoking (0/1)" onChange={handleChange} required />
        <button type="submit">Predict</button>
      </form>
      {result && <h3>Result: {result}</h3>}
    </div>
  );
}

export default App;