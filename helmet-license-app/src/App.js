import { useState } from "react";
import "./App.css";

function App() {
  const [numberPlate, setNumberPlate] = useState();
  const [data, setData] = useState([]);

  const fetchData = async () => {
    try {
      const response = await fetch(
        "http://localhost:8080/get_violations?no=" + numberPlate
      );
      const data = await response.json();
      setData(data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="App">
      <div className="search-container">
        <input
          type="text"
          placeholder="Enter number plate"
          value={numberPlate}
          onChange={(e) => setNumberPlate(e.target.value)}
          className="search-input"
        />
        <button onClick={fetchData} className="search-button">
          Search
        </button>
      </div>
      {data.map((item, index) => {
        return (
          <div key={index} className="data-item">
            <p>Number Plate: {item.no}</p>
            <p>TimeStamp: {item.timestamp}</p>
            <img src={item.proof} alt="number plate" className="data-image" />
          </div>
        );
      })}
    </div>
  );
}

export default App;
