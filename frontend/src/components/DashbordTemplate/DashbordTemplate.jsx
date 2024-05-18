import React, { useState, useEffect } from 'react';
import { getListObjectsFromServer } from '../../api/getListObjectsFromServer';

import { FilterList } from '../FiltersList/FiltersList';

import { CampaignDashboardCard } from '../DashboardCards/CampaignDashboardCard/CampaignDashboardCard';
import { ClickDashboardCard } from '../DashboardCards/ClickDashboardCard/ClickDashboardCard';
import { LeadDashboardCard } from '../DashboardCards/LeadDashboardCard/LeadDashboardCard';
import { OfferDashboardCard } from '../DashboardCards/OfferDashboardCard/OfferDashboardCard';


export const DashboardList = ({ filtersObj, objectType, orderingType } ) => {
  const [listObjects, setListObjects] = useState([]);
  const [filters, setFilters] = useState(filtersObj);
  const [ordering, setOrdering] = useState(orderingType[0]);
  const [currentPage, setCurrentPage] = useState(0);
  const [totalPages, setTotalPages] = useState(1);
  const itemsPerPage = 9

  const fetchListObjects = async (objectType, query, limit, offset, ordering) => {
    try {
      const data = await getListObjectsFromServer(objectType.toLowerCase(), { ...query, ordering }, limit, offset);
      setListObjects(data.results);
      setTotalPages(Math.ceil(data.count / limit));
    } catch (err) {
      console.log(err.message);
    }
  };

  useEffect(() => {
    fetchListObjects(objectType, filters, itemsPerPage, currentPage * itemsPerPage, ordering);
  }, [objectType, filters, itemsPerPage, currentPage, ordering]);

  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters((prevFilters) => ({ ...prevFilters, [name]: value }));
    setCurrentPage(0); 
  };

  const handleOrderingChange = (e) => {
    setOrdering(e.target.value);
  };


  const handleNextPage = () => {
    if (currentPage < totalPages - 1) {
      setCurrentPage((prevPage) => prevPage + 1);
    }
  };

  const handlePreviousPage = () => {
    if (currentPage > 0) {
      setCurrentPage((prevPage) => prevPage - 1);
    }
  };
  
  const renderCardComponent = (item) => {
    switch (objectType) {
      case "Campaigns":
        return <CampaignDashboardCard campaign={item} key={item.id} />;
      case "Leads":
        return <LeadDashboardCard lead={item} key={item.id} />;
      case "Offers":
        return <OfferDashboardCard offer={item} key={item.id} />;
      case "Clicks":
        return <ClickDashboardCard click={item} key={item.id} />;
      default:
        return null;
    }
  };


  return (
    <>
      <h2 className="Dashboard__title">{ objectType } Dashboard</h2>
      <div>
        <div className="Dashboard__filter">Filters:</div>
        <FilterList filtersObj={filters} handleFilterChange={handleFilterChange} />
        <select className="Dashboard__ordering" value={ordering} onChange={handleOrderingChange}>
          {orderingType.map((orderingChoice) => (
            <option key={orderingChoice} value={orderingChoice}>
              {orderingChoice.charAt(0).toUpperCase() + orderingChoice.slice(1)}
            </option>
          ))}
        </select>
      </div>

      <ol className='Dashboard__list'>
      <ol className="Dashboard__list">
        {listObjects.map((item) => renderCardComponent(item))}
      </ol>
        </ol>
        <div className="pagination">
            <button className="pagination__arrow pagination__arrow__right" onClick={handlePreviousPage} disabled={currentPage === 0}>
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M15 18l-6-6 6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
            <button className="pagination__arrow pagination__arrow__left" onClick={handleNextPage} disabled={currentPage >= totalPages - 1}>
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
               <path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
             </svg>
            </button>
          </div>
    </>
  );
};

export default DashboardList;
