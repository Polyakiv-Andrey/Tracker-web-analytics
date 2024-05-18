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
    </section>
  );
};



export default App;

