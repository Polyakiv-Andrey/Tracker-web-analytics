import './ClickDashboardCard.scss';
import formatDate from '../../../utils/formatDate';


export const ClickDashboardCard = ({ click }) => {
  return (
    <li className="Click__card">
      <div className="Click__card__click_time">Click time: {formatDate(click.click_time)}</div>
      <div className="Click__card__click_url">Url: <a href={ click.click_url }>{click.click_url}</a></div>
      <div className="Click_card__user_agent">User agent: {click.user_agent}</div>
      <div className="Click_card__ip_address">IP: {click.ip_address}</div>
      <div className="Click_card__operating_system">OS: {click.operating_system}</div>
    </li>
  );
};

export default ClickDashboardCard;