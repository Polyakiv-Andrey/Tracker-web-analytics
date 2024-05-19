export const formatDate = (dateString) => {
  const options = { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric', 
    hour: '2-digit', 
    minute: '2-digit', 
    second: '2-digit', 
    timeZone: 'UTC'
  };
  return new Date(dateString).toLocaleDateString(undefined, options);
};

export default formatDate;