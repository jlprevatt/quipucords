import React from 'react';
import configureMockStore from 'redux-mock-store';
import ScanListItem from '../scanListItem';
import { mount } from 'enzyme';
import { viewTypes } from '../../../redux/constants/';

describe('SourceListItem Component', function() {
  const generateEmptyStore = () => configureMockStore()({ sources: {}, viewOptions: { [viewTypes.SCANS_VIEW]: {} } });

  it('should render a basic component with a success status', () => {
    const store = generateEmptyStore();
    const props = {
      item: {
        id: 1,
        most_recent: {
          status: 'success'
        }
      }
    };

    const component = mount(<ScanListItem {...props} />, { context: { store } });

    expect(component.render()).toMatchSnapshot();
  });
});
