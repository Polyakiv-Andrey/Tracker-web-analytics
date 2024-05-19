import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';
import { BASE_URL } from '../../constants';
import './AnalyticsDashboard.scss';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export const AnalyticsDashboard = ({ url }) => {
  const [data, setData] = useState({
    labels: [],
    datasets: [
      {
        label: 'Lead amount',
        data: [],
        borderColor: 'rgba(75,192,192,1)',
        backgroundColor: 'rgba(75,192,192,0.2)',
      },
    ],
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(BASE_URL + url);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        console.log('Fetched data:', result); 

        const formattedData = {
          labels: result.data.map(entry => entry.day),
          datasets: [
            {
              label: result.data[0].table_name,
              data: result.data.map(entry => entry.statistic),
              borderColor: 'rgba(75,192,192,1)',
              backgroundColor: 'rgba(75,192,192,0.2)',
            },
          ],
        };
        setData(formattedData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [url]);

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Analytics Dashboard',
      },
    },
  };

  return (
    <div className="analytics-chart">
      <Line data={data} options={options} />
    </div>
  );
};

export default AnalyticsDashboard;
