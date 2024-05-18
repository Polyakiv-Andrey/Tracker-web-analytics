import './LeadDashboardCard.scss';
import formatDate from '../../../utils/formatDate';


export const LeadDashboardCard = ({ lead }) => {
  return (
    <li className="Lead__card">
      <div className="Lead__card__user">Lead user: {lead.user}</div>
      <div className="Lead__card__action">Lead action: {lead.action}</div>
      <div className="Lead_card__date">Lead date: {formatDate(lead.date)}</div>
      <div className="Lead_card__date">Level of interst: {lead.interest_level}</div>
    </li>
  );
};

export default LeadDashboardCard;