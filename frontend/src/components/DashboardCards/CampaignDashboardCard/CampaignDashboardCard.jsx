import formatDate from '../../../utils/formatDate';

export const CampaignDashboardCard = ({ campaign }) => {
  return (
    <li className="Campaign__card">
      <div>Campaign name: {campaign.name}</div>
      <div>Start date: {formatDate(campaign.start_date)}</div>
      <div>End date: {formatDate(campaign.end_date)}</div>
      <div>Goal: { campaign.goal }</div>
    </li>
  )
};
export default CampaignDashboardCard;