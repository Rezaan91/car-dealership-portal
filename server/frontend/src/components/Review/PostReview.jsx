import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

function PostReview() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [dealer, setDealer] = useState(null);
  const [carMakes, setCarMakes] = useState([]);
  const [formData, setFormData] = useState({
    dealer: id,
    purchase: false,
    purchase_date: '',
    car_make: '',
    car_model: '',
    car_year: '',
    review_text: ''
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchDealer();
    fetchCarMakes();
  }, [id]);

  const fetchDealer = async () => {
    try {
      const response = await axios.get(`/api/dealers/${id}/`);
      setDealer(response.data);
    } catch (error) {
      console.error('Error fetching dealer:', error);
    }
  };

  const fetchCarMakes = async () => {
    try {
      const response = await axios.get('/api/cars/makes/');
      setCarMakes(response.data);
    } catch (error) {
      console.error('Error fetching car makes:', error);
    }
  };

  const handleChange = (e) => {
    const value = e.target.type === 'checkbox' ? e.target.checked : e.target.value;
    setFormData({
      ...formData,
      [e.target.name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await axios.post('/api/reviews/', formData);
      console.log('Review posted:', response.data);
      alert('Review posted successfully!');
      navigate(`/dealer/${id}`);
    } catch (error) {
      console.error('Error posting review:', error);
      if (error.response && error.response.data) {
        setError(JSON.stringify(error.response.data));
      } else {
        setError('Failed to post review. Please try again.');
      }
      setLoading(false);
    }
  };

  if (!dealer) {
    return (
      <div className="container mt-5 text-center">
        <div className="spinner-border" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8">
          <div className="card">
            <div className="card-body">
              <h2 className="card-title mb-4">Post Review for {dealer.name}</h2>
              
              {error && (
                <div className="alert alert-danger" role="alert">
                  {error}
                </div>
              )}

              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label className="form-label">Review Text *</label>
                  <textarea
                    className="form-control"
                    name="review_text"
                    rows="5"
                    value={formData.review_text}
                    onChange={handleChange}
                    required
                    placeholder="Share your experience with this dealer..."
                  />
                </div>

                <div className="mb-3 form-check">
                  <input
                    type="checkbox"
                    className="form-check-input"
                    id="purchase"
                    name="purchase"
                    checked={formData.purchase}
                    onChange={handleChange}
                  />
                  <label className="form-check-label" htmlFor="purchase">
                    I purchased a vehicle from this dealer
                  </label>
                </div>

                {formData.purchase && (
                  <>
                    <div className="mb-3">
                      <label className="form-label">Purchase Date</label>
                      <input
                        type="date"
                        className="form-control"
                        name="purchase_date"
                        value={formData.purchase_date}
                        onChange={handleChange}
                      />
                    </div>

                    <div className="mb-3">
                      <label className="form-label">Car Make</label>
                      <select
                        className="form-select"
                        name="car_make"
                        value={formData.car_make}
                        onChange={handleChange}
                      >
                        <option value="">Select Make</option>
                        {carMakes.map((make) => (
                          <option key={make.id} value={make.name}>
                            {make.name}
                          </option>
                        ))}
                      </select>
                    </div>

                    <div className="mb-3">
                      <label className="form-label">Car Model</label>
                      <input
                        type="text"
                        className="form-control"
                        name="car_model"
                        value={formData.car_model}
                        onChange={handleChange}
                        placeholder="e.g., Camry, Civic, etc."
                      />
                    </div>

                    <div className="mb-3">
                      <label className="form-label">Car Year</label>
                      <input
                        type="number"
                        className="form-control"
                        name="car_year"
                        value={formData.car_year}
                        onChange={handleChange}
                        min="1900"
                        max={new Date().getFullYear() + 1}
                        placeholder="e.g., 2023"
                      />
                    </div>
                  </>
                )}

                <div className="d-flex gap-2">
                  <button
                    type="submit"
                    className="btn btn-primary"
                    disabled={loading}
                  >
                    {loading ? 'Posting...' : 'Post Review'}
                  </button>
                  <button
                    type="button"
                    className="btn btn-secondary"
                    onClick={() => navigate(`/dealer/${id}`)}
                  >
                    Cancel
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default PostReview;
