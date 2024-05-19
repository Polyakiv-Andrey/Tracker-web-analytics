import './App.scss';
import { DashboardList } from './components/DashbordTemplate/DashbordTemplate'

export const App = () => {
  return (
    <section className="App">
      <DashboardList
        filtersObj={{ name: '', goal: '', start_date: '', end_date: '' }}
        objectType="Campaigns"
        orderingType={["name", "goal", "start_date", "end_date"]}
      />
      <DashboardList
        filtersObj={{ title: '', url: '', campaigns: '', }}
        objectType="Offers"
        orderingType={["title", "url", "campaigns"]}
      />
      <DashboardList
        filtersObj={{ user: '', action: '', date: '', interest_level: '' }}
        objectType="Leads"
        orderingType={["user", "action", "date", "interest_level"]}
      />
      <DashboardList
        filtersObj={{ click_date_gte: '', click_date_lte: '',click_url: '', user_agent: '', ip_address: '', operating_system: '' }}
        objectType="Clicks"
        orderingType={["click_time", "click_url", "user_agent", "ip_address", "operating_system"]}
      />
    </section>
  );
};


export default App;

