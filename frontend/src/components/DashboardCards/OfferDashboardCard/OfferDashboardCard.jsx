import './OfferDashboardCard.scss';

export const OfferDashboardCard = ({ offer }) => {
  return (
    <li className="Offer__card">
      <div className="Offer__card__title">Offer title: {offer.title}</div>
      <div className="Offer__card__url">Offer url: <a href={offer.url}>{offer.url}</a></div>
      <div className="Offer__card__date">Offer campaign: {offer.campaigns.name}</div>
    </li>
  );
};

export default OfferDashboardCard;