import formatDate from '../../../utils/formatDate';
import './CampaignDashboardCard.scss';

export const CampaignDashboardCard = ({ campaign }) => {
  return (
    <li className="Campaign__card">
      <div className="Campaign__card__title">Campaign name: {campaign.name}</div>
      <div className="Campaign__card__date">Start date: {formatDate(campaign.start_date)}</div>
      <div className="Campaign__card__date">End date: {formatDate(campaign.end_date)}</div>
      <div className="Campaign__card__goal">Goal: {campaign.goal}</div>
    </li>
  );
};

export default CampaignDashboardCard;