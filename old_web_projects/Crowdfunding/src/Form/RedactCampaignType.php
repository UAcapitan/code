<?php

namespace App\Form;

use App\Entity\Campaigns;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\Extension\Core\Type\IntegerType;
use Symfony\Component\Form\Extension\Core\Type\DateType;
use Symfony\Component\Form\Extension\Core\Type\ChoiceType;

class RedactCampaignType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options)
    {
        $builder
            ->add('name', TextType::class, [
                'label' => false,
                'attr' => ['placeholder' => 'Name'],
            ])
            ->add('description', TextType::class, [
                'label' => false,
                'attr' => ['placeholder' => 'Description'],
            ])
            ->add('video', TextType::class, [
                'label' => false,
                'attr' => ['placeholder' => 'Video'],
            ])
            ->add('money', IntegerType::class, [
                'label' => false,
                'attr' => ['placeholder' => 'Money'],
            ])
            ->add('subject', ChoiceType::class, [
                'label' => 'Subject: ',
                'choices'  => [
                    'Device' => 'Device',
                    'Event' => 'Event',
                    'Game' => 'Game',
                    'Program' => 'Program',
                    'Other' => 'Other',
                ]])
        ;
    }

    public function configureOptions(OptionsResolver $resolver)
    {
        $resolver->setDefaults([
            'data_class' => Campaigns::class,
        ]);
    }
}
