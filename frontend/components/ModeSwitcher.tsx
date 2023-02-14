'use client';

import { Tab } from "@headlessui/react";
import FilteredRandom from "./FilteredRandom";
import PickAndPass from "./PickAndPass";

type SwitcherProps = {
  mode: string,
  withData: boolean
};

export default function ModeSwitcher({ mode, withData }: SwitcherProps) {
  return (
    <Tab.Group>
      <Tab.List>
        <Tab key={"Filtered Random"}>
          Filtered Random
        </Tab>
        <Tab key={"Pick and Pass"}>
          Pick and Pass
        </Tab>
      </Tab.List>
      <Tab.Panels>
        <Tab.Panel>
          <FilteredRandom />
        </Tab.Panel>
        <Tab.Panel>
          <PickAndPass />
        </Tab.Panel>
      </Tab.Panels>
    </Tab.Group>
  )
}