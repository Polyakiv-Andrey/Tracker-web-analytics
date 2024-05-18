import React from 'react';
import './FiltersList.scss';

export const FilterList = ({ filtersObj, handleFilterChange }) => {
  const renderFilters = () => {
    return Object.keys(filtersObj).map((key) => {
      let type = "text";
      if (key.includes("date")) {
        type = "datetime-local";
      }
      return (
        <div className='Dashboard__filters__element'>
        <span className='Dashboard__filters__title'>{ key.charAt(0).toUpperCase() + key.slice(1) }: </span>
        <input
          key={key}
          className="Dashboard__filter__input"
          type={type}
          name={key}
          placeholder={key.charAt(0).toUpperCase() + key.slice(1)}
          value={filtersObj[key]}
          onChange={handleFilterChange}
          />
        </div>
      );
    });
  };

  return (
    <div className="Dashboard__filters">
      {renderFilters()}
    </div>
  );
};

export default FilterList;