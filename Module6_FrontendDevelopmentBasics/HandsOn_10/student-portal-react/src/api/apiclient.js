import axios from 'axios';

const apiClient=axios.create({
  baseURL:'https://jsonplaceholder.typicode.com',
  headers:{
    'Content-Type':'application/json'
  },
  timeout:5000
});

apiClient.interceptors.request.use(
  config=>{
    config.headers.Authorization='Bearer mock_jwt_token_auth_10';
    return config;
  },
  error=>Promise.reject(error)
);

apiClient.interceptors.response.use(
  response=>response.data,
  error=>{
    const customError={
      message:error.response?.data?.message || error.message || 'API Communication Error',
      statusCode:error.response?.status || 500
    };
    return Promise.reject(customError);
  }
);

export default apiClient;