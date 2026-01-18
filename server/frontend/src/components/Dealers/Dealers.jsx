import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './Dealers.css';

function Dealers() {
  const [dealers, setDealers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDealers();
  }, []);

  const fetchDealers = async () => {
    try {
      const response = await axios.get('/api/dealers/');
      setDealers(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching dealers:', error);
      setLoading(false);
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center text-white mb-4">All Dealers</h1>

      {loading ? (
        <div className="text-center">
          <div className="spinner-border text-light" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      ) : (
        <div className="row">
          {dealers.map((dealer) => (
            <div key={dealer.id} className="col-md-4 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">{dealer.name}</h5>
                  <p className="card-text">
                    <strong>Location:</strong> {dealer.city}, {dealer.state}
                  </p>
                  <p className="card-text">
                    <strong>Address:</strong> {dealer.address}
                  </p>
                  <p className="card-text">
                    <strong>Phone:</strong> {dealer.phone}
                  </p>
                  <Link to={`/dealer/${dealer.id}`} className="btn btn-primary">
                    View Details
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Dealers;
