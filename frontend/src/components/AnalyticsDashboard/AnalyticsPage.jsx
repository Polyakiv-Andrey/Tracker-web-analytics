import React from 'react';
import { AnalyticsDashboard } from './AnalyticsDashboard';
import './AnalyticsDashboard.scss';

export const AnalyticsPage = () => {
  return (
    <div className="analytics-container">
      <AnalyticsDashboard url="analytics/clicks/" />
      <AnalyticsDashboard url="analytics/leads/" />
      <AnalyticsDashboard url="analytics/conversions/" />
      <AnalyticsDashboard url="analytics/revenue/" />
      <AnalyticsDashboard url="analytics/epc/" />
    </div>
  );
};

export default AnalyticsPage;
